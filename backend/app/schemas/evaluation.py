from datetime import datetime
from pydantic import BaseModel, ConfigDict


class EvaluationCreate(BaseModel):
    dataset_id: int
    provider: str
    model_name: str


class EvaluationResponse(BaseModel):
    id: int
    user_id: int
    dataset_id: int
    provider: str
    model_name: str
    status: str
    total_prompts: int
    completed_prompts: int
    started_at: datetime | None
    completed_at: datetime | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)