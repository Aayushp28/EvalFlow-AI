from app.core.config import settings

from app.evaluation.providers.gemini_provider import GeminiProvider
from app.evaluation.providers.openai_provider import OpenAIProvider
from app.evaluation.providers.claude_provider import ClaudeProvider


class ProviderFactory:

    @staticmethod
    def create(provider_name: str):

        provider = provider_name.lower()

        if provider == "gemini":
            return GeminiProvider()

        if provider == "openai":
            return OpenAIProvider()

        if provider == "claude":
            return ClaudeProvider()

        raise ValueError(
            f"Unsupported provider: {provider_name}"
        )