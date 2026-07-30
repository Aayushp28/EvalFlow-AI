import re
import time

from google import genai

from app.core.config import settings
from app.evaluation.providers.base import BaseProvider


class GeminiProvider(BaseProvider):

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def generate(self, prompt: str) -> str:

        while True:

            try:

                response = self.client.models.generate_content(
                    model=settings.GEMINI_MODEL,
                    contents=prompt,
                )

                return response.text

            except Exception as e:

                error = str(e)

                # Handle Gemini free-tier rate limit
                if "RESOURCE_EXHAUSTED" in error or "429" in error:

                    wait = 45

                    match = re.search(
                        r"retryDelay': '(\d+)s'",
                        error
                    )

                    if match:
                        wait = int(match.group(1)) + 2

                    print("\n" + "=" * 60)
                    print("⚠ Gemini API Rate Limit Reached")
                    print(f"Waiting {wait} seconds before retrying...")
                    print("=" * 60 + "\n")

                    time.sleep(wait)

                    continue

                # Any other error should be raised
                raise