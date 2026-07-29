from app.evaluation.providers.gemini_provider import GeminiProvider

provider = GeminiProvider()

response = provider.generate(
    "What is Artificial Intelligence?"
)

print(response)