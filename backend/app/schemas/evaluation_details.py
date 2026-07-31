from datetime import datetime

from pydantic import BaseModel


class EvaluationResultItem(BaseModel):

    id: int

    prompt: str

    response: str

    latency: float

    input_tokens: int

    output_tokens: int

    total_tokens: int

    estimated_cost: float

    score: float | None

    feedback: str | None


class EvaluationInfo(BaseModel):

    id: int

    dataset_name: str

    provider: str

    model_name: str

    status: str

    total_prompts: int

    completed_prompts: int

    created_at: datetime


class EvaluationDetailsResponse(BaseModel):

    evaluation: EvaluationInfo

    results: list[EvaluationResultItem]