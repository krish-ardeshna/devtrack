from pydantic import BaseModel
from datetime import datetime

class TaskBase(BaseModel):
    title: str

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    status: str
    created_at: datetime
    repo_link: str | None = None