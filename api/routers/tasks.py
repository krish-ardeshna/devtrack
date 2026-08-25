from fastapi import APIRouter, HTTPException, Depends
from typing import List

from schemas.task import TaskResponse, TaskCreate
from core.dependencies import get_storage
from storage import Storage
from task import Task

router = APIRouter(tags=["tasks"])

@router.get("/", response_model=List[TaskResponse])
def get_tasks(storage: Storage = Depends(get_storage)):
    return [t.to_dict() for t in storage.tasks]

@router.post("/", response_model=TaskResponse)
def create_task(task_in: TaskCreate, storage: Storage = Depends(get_storage)):
    task = Task(title=task_in.title)
    storage.add_task(task)
    return task.to_dict()

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_in: TaskCreate, storage: Storage = Depends(get_storage)):
    ok = storage.update_task(task_id, title=task_in.title)
    if not ok:
        raise HTTPException(status_code=404, detail="Task not found")
    return storage.get_task(task_id).to_dict()

@router.post("/{task_id}/complete", response_model=TaskResponse)
def complete_task(task_id: int, storage: Storage = Depends(get_storage)):
    ok = storage.complete_task(task_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Task not found")
    return storage.get_task(task_id).to_dict()

@router.delete("/{task_id}")
def delete_task(task_id: int, storage: Storage = Depends(get_storage)):
    ok = storage.delete_task(task_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted"}