from task import Task
from status import Status
import datetime

def test_constructor_defaults():
    task = Task("Test Task")
    
    assert task.title == "Test Task"
    assert task.status == Status.PENDING
    assert isinstance(task.created_at, datetime.datetime)
    assert task.repo_link is None

def test_to_dict_keys_and_types():
    task = Task("Test Task")
    task_dict = task.to_dict()
    
    assert isinstance(task_dict, dict)
    assert set(task_dict.keys()) == {"id", "title", "status", "created_at", "repo_link"}
    assert isinstance(task_dict["status"], str)
    assert isinstance(task_dict["created_at"], str) 

def test_from_dict_round_trip():
    task = Task("Test Task")
    task_dict = task.to_dict()
    reconstructed_task = Task.from_dict(task_dict)
    
    assert reconstructed_task.id == task.id
    assert reconstructed_task.title == task.title
    assert reconstructed_task.status == task.status
    assert reconstructed_task.created_at.isoformat() == task.created_at.isoformat()
    assert reconstructed_task.repo_link == task.repo_link

def test_complete_idempotent():
    task = Task("Test Task")
    
    task.complete()
    assert task.status == Status.COMPLETED
    
    task.complete()
    assert task.status == Status.COMPLETED