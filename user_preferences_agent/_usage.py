import pydantic
from openai.types.responses.response_usage import (
    InputTokensDetails,
    OutputTokensDetails,
)


class Usage(pydantic.BaseModel):
    requests: int = 0
    input_tokens: int = 0
    input_tokens_details: InputTokensDetails = pydantic.Field(
        default_factory=lambda: InputTokensDetails(cached_tokens=0)
    )
    output_tokens: int = 0
    output_tokens_details: OutputTokensDetails = pydantic.Field(
        default_factory=lambda: OutputTokensDetails(reasoning_tokens=0)
    )
    total_tokens: int = 0
