from datetime import datetime
from pydantic import BaseModel, ConfigDict


class DatasetResponse(BaseModel):
    id: int
    filename: str
    original_name: str
    file_type: str
    file_size: int
    upload_date: datetime

    model_config = ConfigDict(from_attributes=True)