import enum
import datetime
from status import Status
from typing import Optional

class Task:
    def __init__(
            self,
            title: str, 
            id: int | None = None,
            status: Status = Status.PENDING, 
            created_at: datetime.datetime | None = None, 
            repo_link: Optional[str] = None
        ):
        self.id = id
        self.title = title
        self.status = status
        self.created_at = created_at if created_at is not None else datetime.datetime.now()
        self.repo_link = repo_link
        
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "repo_link": self.repo_link,
        }
        
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            title=data["title"],
            status=Status(data["status"]),
            created_at=datetime.datetime.fromisoformat(data["created_at"]) if data.get("created_at") else None,
            repo_link=data.get("repo_link"),
        )
        
    def complete(self):
        if self.status == Status.COMPLETED:
            print(f"Task '{self.title}' is already completed.")
            return self
        self.status = Status.COMPLETED
        return self
    
    def __repr__(self):
        return f"Task(id={self.id}, title={self.title}, status={self.status.value})"

