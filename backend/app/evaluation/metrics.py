class Metrics:

    """
    Utility methods for evaluation metrics.
    """

    @staticmethod
    def estimate_cost(total_tokens: int) -> float:
        """
        Placeholder cost estimation.

        Replace with actual provider pricing later.
        """

        return round(total_tokens * 0.0000005, 8)