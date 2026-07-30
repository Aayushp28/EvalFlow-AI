import json
import re

from app.evaluation.providers.gemini_provider import GeminiProvider


class Judge:

    def __init__(self):
        self.provider = GeminiProvider()

    def score(
        self,
        prompt: str,
        response: str
    ) -> tuple[float, str]:
        """
        Uses Gemini to evaluate a generated response.
        Returns:
            (score, feedback)
        """

        judge_prompt = f"""
You are an expert AI evaluator.

Evaluate the following AI response.

Question:
{prompt}

Response:
{response}

Score the response from 0 to 10 based on:
- Correctness
- Completeness
- Clarity
- Relevance

Return ONLY valid JSON.

Example:

{{
    "score": 9.2,
    "feedback": "Accurate, clear and well-structured."
}}
"""

        try:

            result = self.provider.generate(judge_prompt)

            # Remove Markdown code fences if present
            cleaned = result.strip()

            cleaned = re.sub(
                r"^```json\s*",
                "",
                cleaned,
                flags=re.IGNORECASE
            )

            cleaned = re.sub(
                r"^```",
                "",
                cleaned
            )

            cleaned = re.sub(
                r"```$",
                "",
                cleaned
            ).strip()

            data = json.loads(cleaned)

            score = float(data.get("score", 0))

            # Clamp score between 0 and 10
            score = max(0.0, min(score, 10.0))

            feedback = data.get(
                "feedback",
                "No feedback provided."
            )

            return (
                score,
                feedback
            )

        except Exception as e:

            print(f"Judge Error: {e}")

            return (
                0.0,
                "Unable to evaluate response."
            )