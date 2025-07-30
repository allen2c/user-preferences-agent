import agents
import logging_bullet_train as lbt
import openai
import pytest

lbt.set_logger("ner_agent")
lbt.set_logger("tests")


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
