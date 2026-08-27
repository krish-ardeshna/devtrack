from pydantic import BaseModel
from datetime import datetime, date

class TaskBase(BaseModel):
    title: str

class TaskCreate(TaskBase):
    repo_link: str | None = None
    priority: str = "medium"
    tags: list[str] = []
    due_date: date | None = None

class TaskUpdate(BaseModel):
    title: str | None = None
    repo_link: str | None = None
    priority: str | None = None
    tags: list[str] | None = None
    due_date: date | None = None

class TaskResponse(TaskBase):
    id: int
    status: str
    created_at: datetime
    repo_link: str | None = None
    priority: str
    tags: list[str]
    due_date: date | None = None