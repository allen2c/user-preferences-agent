# user_preferences_agent/__init__.py
import json
import logging
import pathlib
import re
import textwrap
import typing
from dataclasses import asdict

import agents
import jinja2
import openai
import pydantic
from google_language_support import LanguageCodes
from openai.types import ChatModel
from str_or_none import str_or_none

from user_preferences_agent._currency import CurrencyCode
from user_preferences_agent._timezone import TimezoneCode

__version__ = pathlib.Path(__file__).parent.joinpath("VERSION").read_text().strip()

logger = logging.getLogger(__name__)

DEFAULT_MODEL = "gpt-4.1-nano"
ResponseStyle = typing.Literal["concise", "detailed", "professional", "casual"]
Persona = typing.Literal["neutral_assistant", "expert_tutor", "creative_partner"]
EmojiUsageLevel = typing.Literal["none", "sparingly", "frequent"]


class UserPreferences(pydantic.BaseModel):
    """Represents all user-configurable preferences."""

    # --- General & Localization Settings ---
    language: LanguageCodes | None = pydantic.Field(
        default=None,
        description="The language the user prefers to use for the interface and responses.",  # noqa: E501
    )

    timezone: TimezoneCode | None = pydantic.Field(
        default=None,
        description="The timezone the user is currently in for accurate time-sensitive information.",  # noqa: E501
    )

    currency: CurrencyCode | None = pydantic.Field(
        default=None,
        description="The currency ISO 4217 code the user prefers for financial information.",  # noqa: E501
    )

    country: str | None = pydantic.Field(
        default=None,
        description="The country the user is located in, for regional context.",  # noqa: E501
    )

    city: str | None = pydantic.Field(
        default=None,
        description="The city the user is located in, for more specific local context.",  # noqa: E501
    )

    # --- AI Memory & Core Instructions ---
    rules_and_memories: typing.List[str] = pydantic.Field(
        default_factory=list,
        description="A list of standing rules, facts, and memories for the AI to follow.",  # noqa: E501
    )


class UserPreferencesAgent:
    instructions: str = textwrap.dedent(
        """
        """
    )

    async def run(
        self,
        text: str,
        *,
        model: (
            agents.OpenAIChatCompletionsModel
            | agents.OpenAIResponsesModel
            | ChatModel
            | str
            | None
        ) = None,
        tracing_disabled: bool = True,
        verbose: bool = False,
        **kwargs,
    ) -> "UserPreferencesResult":
        if str_or_none(text) is None:
            raise ValueError("text is required")

        chat_model = self._to_chat_model(model)

        agent_instructions: str = (
            jinja2.Template(self.instructions).render(text=text).strip()
        )

        if verbose:
            print("\n\n--- LLM INSTRUCTIONS ---\n")
            print(agent_instructions)

        agent = agents.Agent(
            name="user-preferences-agent",
            model=chat_model,
            model_settings=agents.ModelSettings(temperature=0.0),
            instructions=agent_instructions,
        )
        result = await agents.Runner.run(
            agent, text, run_config=agents.RunConfig(tracing_disabled=tracing_disabled)
        )

        if verbose:
            print("\n\n--- LLM OUTPUT ---\n")
            print(str(result.final_output))
            print("\n--- LLM USAGE ---\n")
            print(
                "Usage:",
                json.dumps(
                    asdict(result.context_wrapper.usage),
                    ensure_ascii=False,
                    default=str,
                ),
            )

        return UserPreferencesResult(
            text=text,
            user_preferences=self._parse_user_preferences(str(result.final_output)),
        )

    def _parse_user_preferences(
        self,
        text: str,
    ) -> UserPreferences:
        pass

    def _to_chat_model(
        self,
        model: (
            agents.OpenAIChatCompletionsModel
            | agents.OpenAIResponsesModel
            | ChatModel
            | str
            | None
        ) = None,
    ) -> agents.OpenAIChatCompletionsModel | agents.OpenAIResponsesModel:
        model = DEFAULT_MODEL if model is None else model

        if isinstance(model, str):
            openai_client = openai.AsyncOpenAI()
            return agents.OpenAIResponsesModel(
                model=model,
                openai_client=openai_client,
            )

        else:
            return model


class UserPreferencesResult(pydantic.BaseModel):
    text: str
    user_preferences: UserPreferences
