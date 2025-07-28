import json
import typing

import pydantic
from openai.types.responses import ResponseInputItemParam


class Message(pydantic.BaseModel):
    role: typing.Literal["user", "assistant"] | str
    content: str
    created_at: int | None = None

    @classmethod
    def from_data(cls, data: pydantic.BaseModel | dict) -> "Message":
        _data = (
            json.loads(data.model_dump_json())
            if isinstance(data, pydantic.BaseModel)
            else data
        )
        return cls.model_validate(_data)

    @classmethod
    def from_response_input_item_param(cls, data: ResponseInputItemParam) -> "Message":
        return cls.from_data(data)

    @classmethod
    def from_response_input_item_params(
        cls, data: list[ResponseInputItemParam]
    ) -> list["Message"]:
        return [cls.from_data(i) for i in data]
