from fastapi import APIRouter, Depends, HTTPException
from typing import List
import httpx

from core.dependencies import get_http_client
from services.github_service import fetch_repo_summary, fetch_commit_summaries
from schemas.github import RepoSummary, CommitSummary

router = APIRouter(tags=["github"])

@router.get("/repo", response_model=RepoSummary)
async def get_repo_info(client: httpx.AsyncClient = Depends(get_http_client)):
    try:
        return await fetch_repo_summary(client)
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail="GitHub API error")
    except httpx.RequestError:
        raise HTTPException(status_code=503, detail="Unable to connect to GitHub API")

@router.get("/commits", response_model=List[CommitSummary])
async def get_commits(client: httpx.AsyncClient = Depends(get_http_client)):
    try:
        return await fetch_commit_summaries(client)
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail="GitHub API error")
    except httpx.RequestError:
        raise HTTPException(status_code=503, detail="Unable to connect to GitHub API")