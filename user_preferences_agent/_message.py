import json
import typing

import pydantic
from openai.types.responses.easy_input_message_param import EasyInputMessageParam
from openai.types.responses.response_input_item_param import Message as ResponseMessage
from openai.types.responses.response_input_item_param import (
    ResponseInputItemParam,
)
from openai.types.responses.response_output_message_param import (
    ResponseOutputMessageParam,
)


class Message(pydantic.BaseModel):
    role: typing.Literal["user", "assistant"] | str
    content: str

    @classmethod
    def from_data(cls, data: pydantic.BaseModel | dict) -> "Message":
        _data = (
            json.loads(data.model_dump_json())
            if isinstance(data, pydantic.BaseModel)
            else data
        )
        return cls.model_validate(_data)

    @classmethod
    def from_response_input_item_param(
        cls, data: ResponseInputItemParam
    ) -> typing.Optional["Message"]:
        if data.get("type") != "message":
            return None

        data = typing.cast(
            typing.Union[
                EasyInputMessageParam, ResponseMessage, ResponseOutputMessageParam
            ],
            data,
        )

        _content = data["content"]

        if isinstance(_content, str):
            return cls(role=data["role"], content=_content)

        _content_str = ""
        for item in _content:
            if item["type"] == "input_text":
                _content_str += item["text"]

            elif item["type"] == "input_image":
                _content_str += "[image]"

            elif item["type"] == "input_file":
                _content_str += "[file]"

            elif item["type"] == "output_text":
                _content_str += item["text"]

            elif item["type"] == "refusal":
                pass

            else:
                raise ValueError(f"Unsupported content type: {item['type']}")

        return cls(role=data["role"], content=_content_str)

    @classmethod
    def from_response_input_item_params(
        cls, data: list[ResponseInputItemParam]
    ) -> list["Message"]:
        out: list[Message] = []
        for i in data:
            _message = cls.from_response_input_item_param(i)
            if _message is not None:
                out.append(_message)
        return out

    @classmethod
    def to_messages_instructions(cls, messages: list["Message"]) -> str:
        out = ""
        for message in messages:
            out += f"{message.role}:\n{message.content}\n\n"
        return out.strip()
