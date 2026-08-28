from fastapi import APIRouter, HTTPException, Depends, status
from typing import List

from schemas.task import TaskResponse, TaskCreate, TaskUpdate
from core.dependencies import get_storage
from storage import Storage
from task import Task
from priority import Priority

router = APIRouter(tags=["tasks"])

@router.get("/", response_model=List[TaskResponse], status_code=status.HTTP_200_OK)
def get_tasks(storage: Storage = Depends(get_storage)):
    return [t.to_dict() for t in storage.tasks]

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_in: TaskCreate, storage: Storage = Depends(get_storage)):
    task = Task(
        title=task_in.title,
        repo_link=task_in.repo_link,
        priority=Priority(task_in.priority),
        tags=task_in.tags,
        due_date=task_in.due_date
    )
    storage.add_task(task)
    return task.to_dict()

@router.put("/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def update_task(task_id: int, task_in: TaskUpdate, storage: Storage = Depends(get_storage)):
    priority_val = Priority(task_in.priority) if task_in.priority else None
    ok = storage.update_task(
        task_id,
        title=task_in.title,
        repo_link=task_in.repo_link,
        priority=priority_val,
        tags=task_in.tags,
        due_date=task_in.due_date
    )
    if not ok:
        raise HTTPException(status_code=404, detail="Task not found")
    return storage.get_task(task_id).to_dict()

@router.post("/{task_id}/complete", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def complete_task(task_id: int, storage: Storage = Depends(get_storage)):
    ok = storage.complete_task(task_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Task not found")
    return storage.get_task(task_id).to_dict()

@router.delete("/{task_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, storage: Storage = Depends(get_storage)):
    ok = storage.delete_task(task_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Task not found")
    return None