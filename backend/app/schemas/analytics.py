from pydantic import BaseModel


class AnalyticsSummary(BaseModel):

    total_evaluations: int

    completed_evaluations: int

    pending_evaluations: int

    total_prompts: int

    completed_prompts: int

    average_latency: float

    average_tokens: float

    total_estimated_cost: float

    success_rate: float