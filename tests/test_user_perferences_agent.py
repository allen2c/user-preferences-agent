# tests/test_user_perferences_agent.py
import pathlib
import typing

import agents
import pytest

from user_preferences_agent import UserPreferencesAgent
from user_preferences_agent._message import Message

TEST_CASES_DIR = pathlib.Path(__file__).parent.joinpath("chats")
TEST_CASES: typing.List[typing.Tuple[str, typing.List[Message]]] = [
    (file.name, Message.from_text(file.read_text()))
    for file in TEST_CASES_DIR.glob("*.txt")
]


@pytest.mark.asyncio
@pytest.mark.parametrize("file_name, messages", TEST_CASES)
async def test_user_preferences_agent(
    file_name: str,
    messages: typing.List[Message],
    chat_model: agents.OpenAIChatCompletionsModel | agents.OpenAIResponsesModel,
):
    up_agent = UserPreferencesAgent()
    print(file_name, len(messages))
