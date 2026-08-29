from turtle import title

from task import Task
from task_status import Status
from priority import Priority
import datetime

def test_constructor_defaults():
    task = Task("Test Task")
    
    assert task.title == "Test Task"
    assert task.status == Status.PENDING
    assert isinstance(task.created_at, datetime.datetime)
    assert task.repo_link is None
    assert task.priority == Priority.MEDIUM
    assert task.tags == []
    assert task.due_date is None

def test_to_dict_keys_and_types():
    task = Task("Test Task")
    task_dict = task.to_dict()
    
    assert isinstance(task_dict, dict)
    assert set(task_dict.keys()) == {"id", "title", "status", "created_at", "repo_link", "priority", "tags", "due_date"}
    assert isinstance(task_dict["status"], str)
    assert isinstance(task_dict["created_at"], str)
    assert isinstance(task_dict["priority"], str)
    assert isinstance(task_dict["tags"], list)
    assert task_dict["due_date"] is None or isinstance(task_dict["due_date"], str)

def test_from_dict_round_trip():
    task = Task(
        title="Test Task",
        priority=Priority.HIGH,
        tags=["urgent", "bug"],
        due_date=datetime.date(2026, 9, 1)
    )
    task_dict = task.to_dict()
    reconstructed_task = Task.from_dict(task_dict)

    assert reconstructed_task.id == task.id
    assert reconstructed_task.title == task.title
    assert reconstructed_task.status == task.status
    assert reconstructed_task.created_at.isoformat() == task.created_at.isoformat()
    assert reconstructed_task.repo_link == task.repo_link
    assert reconstructed_task.priority == task.priority
    assert reconstructed_task.tags == task.tags
    assert reconstructed_task.due_date == task.due_date

def test_complete_idempotent():
    task = Task("Test Task")
    
    task.complete()
    assert task.status == Status.COMPLETED
    
    task.complete()
    assert task.status == Status.COMPLETED