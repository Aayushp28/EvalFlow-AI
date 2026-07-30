from typing import Tuple


class Tokenizer:
    """
    Simple token estimator.

    This is an approximation.
    Later we can replace it with provider-specific token counting.
    """

    @staticmethod
    def count(prompt: str, response: str) -> Tuple[int, int, int]:

        input_tokens = len(prompt.split())

        output_tokens = len(response.split())

        total_tokens = input_tokens + output_tokens

        return (
            input_tokens,
            output_tokens,
            total_tokens,
        )