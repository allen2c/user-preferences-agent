import agents
import logging_bullet_train as lbt
import openai
import pytest
import rich.console

lbt.set_logger("openai_usage")
lbt.set_logger("tests")
lbt.set_logger("universal_message")
lbt.set_logger("user_preferences_agent")


@pytest.fixture(scope="module")
def console():
    return rich.console.Console()


@pytest.fixture(scope="module")
def chat_model_str():
    return "gemma3n:e4b"


@pytest.fixture(scope="module")
def chat_model(chat_model_str: str):
    client = openai.AsyncOpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama",
    )
    return agents.OpenAIChatCompletionsModel(model=chat_model_str, openai_client=client)
