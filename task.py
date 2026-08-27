import datetime
from status import Status
from typing import Optional
from priority import Priority

class Task:
    def __init__(
            self,
            title: str, 
            id: int | None = None,
            status: Status = Status.PENDING, 
            created_at: datetime.datetime | None = None, 
            repo_link: Optional[str] = None,
            priority: Priority = Priority.MEDIUM,
            tags: list[str] | None = None,
            due_date: datetime.date | None = None
        ):
        self.id = id
        self.title = title
        self.status = status
        self.created_at = created_at if created_at is not None else datetime.datetime.now()
        self.repo_link = repo_link
        self.priority = priority
        self.tags = tags if tags is not None else []
        self.due_date = due_date
        
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "repo_link": self.repo_link,
            "priority": self.priority.value,
            "tags": self.tags,
            "due_date": self.due_date.isoformat() if self.due_date else None 
        }
        
    @classmethod
    def from_dict(cls, data: dict):
        due_date_str = data.get("due_date")
        parsed_due_date = datetime.date.fromisoformat(due_date_str) if due_date_str else None
        
        return cls(
            id=data.get("id"),
            title=data["title"],
            status=Status(data["status"]),
            created_at=datetime.datetime.fromisoformat(data["created_at"]) if data.get("created_at") else None,
            repo_link=data.get("repo_link"),
            priority=Priority(data.get("priority", "medium")),
            tags=data.get("tags", []),
            due_date=parsed_due_date
        )
        
    def complete(self):
        if self.status == Status.COMPLETED:
            print(f"Task '{self.title}' is already completed.")
            return self
        self.status = Status.COMPLETED
        return self
    
    def __str__(self) -> str:
        tag_str = f" [{', '.join(self.tags)}]" if self.tags else ""
        due_str = f" (Due: {self.due_date})" if self.due_date else ""
        repo_str = f" - {self.repo_link}" if self.repo_link else ""
        
        return f"[{self.id}] {self.title} ({self.status.value}) | Priority: {self.priority.value}{tag_str}{due_str}{repo_str}"
    
    def __repr__(self) -> str:
        return (
            f"Task(id={self.id}, title={self.title!r}, status={self.status.value}, "
            f"priority={self.priority.value}, tags={self.tags}, due_date={self.due_date})"
        )