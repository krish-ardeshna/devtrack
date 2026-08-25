import httpx
from core.config import settings
from schemas.github import RepoSummary, CommitSummary

GITHUB_API_URL = "https://api.github.com/repos/krish-ardeshna/devtrack"

def _auth_headers() -> dict:
    if settings.GITHUB_TOKEN:
        return {"Authorization": f"Bearer {settings.GITHUB_TOKEN}"}
    return {}

async def fetch_repo_summary(client: httpx.AsyncClient) -> RepoSummary:
    response = await client.get(GITHUB_API_URL, headers=_auth_headers())
    response.raise_for_status()
    data = response.json()
    return RepoSummary(
        name=data["name"],
        description=data.get("description"),
        stargazers_count=data["stargazers_count"],
    )

async def fetch_commit_summaries(client: httpx.AsyncClient, per_page: int = 10) -> list[CommitSummary]:
    url = f"{GITHUB_API_URL}/commits?per_page={per_page}"
    response = await client.get(url, headers=_auth_headers())
    response.raise_for_status()
    data = response.json()
    return [
        CommitSummary(message=c["commit"]["message"].split("\n")[0], date=c["commit"]["author"]["date"])
        for c in data
    ]