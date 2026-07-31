from datetime import datetime

from pydantic import BaseModel


class EvaluationHistoryItem(BaseModel):

    id: int

    dataset_name: str

    provider: str

    model_name: str

    status: str

    total_prompts: int

    completed_prompts: int

    created_at: datetime


class EvaluationHistoryResponse(BaseModel):

    evaluations: list[EvaluationHistoryItem]