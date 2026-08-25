from pydantic import BaseModel

class RepoSummary(BaseModel):
    name: str
    description: str | None = None
    stargazers_count: int

class CommitSummary(BaseModel):
    message: str
    date: str