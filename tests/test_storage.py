import datetime
from storage import Storage
from task import Task
from status import Status
from priority import Priority

def test_load_missing_file(tmp_path):
    """Storage pointed at a file that doesn't exist yet → tasks list is empty, no crash"""
    file_path = tmp_path / "tasks.json"
    storage = Storage(str(file_path))
    
    assert len(storage.tasks) == 0
    
def test_add_task_assigns_incrementing_id(tmp_path):
    file_path = tmp_path / "tasks.json"
    storage = Storage(str(file_path))
    
    storage.add_task(Task(title="First Task"))
    storage.add_task(Task(title="Second Task"))
    
    assert storage.get_task(1).id == 1
    assert storage.get_task(2).id == 2
    
def test_get_task_returns_copy_not_reference(tmp_path):
    file_path = tmp_path / "tasks.json"
    storage = Storage(str(file_path))
    storage.add_task(Task(title="Original"))
    
    detached_task = storage.get_task(1)
    detached_task.title = "Hacked task"
    
    safe_task = storage.get_task(1)
    assert safe_task.title == "Original"
    
def test_update_persists_after_reload(tmp_path):
    """key pattern: create Storage, mutate, create a SECOND Storage instance on same path, verify change is there"""
    file_path = tmp_path / "tasks.json"
    storage1 = Storage(str(file_path))
    storage1.add_task(Task(title="Old Title"))
    
    test_date = datetime.date(2026, 9, 1)
    storage1.update_task(
        1, 
        title="New Title",
        repo_link="https://github.com",
        priority=Priority.HIGH,
        tags=["urgent"],
        due_date=test_date
    )
    
    storage2 = Storage(str(file_path))
    task = storage2.get_task(1)
    assert task.title == "New Title"
    assert task.repo_link == "https://github.com"
    assert task.priority == Priority.HIGH
    assert task.tags == ["urgent"]
    assert task.due_date == test_date
    
def test_delete_persits_after_reload(tmp_path):
    file_path = tmp_path / "tasks.json"
    storage1 = Storage(str(file_path))
    storage1.add_task(Task(title="Doomed Task"))
    
    storage1.delete_task(1)
    
    storage2 = Storage(str(file_path))
    assert len(storage2.tasks) == 0
    assert storage2.get_task(1) is None
    
def test_complete_persists_after_reload(tmp_path):
    file_path = tmp_path / "tasks.json"
    storage1 = Storage(str(file_path))
    storage1.add_task(Task(title="Pending Task"))
    
    storage1.complete_task(1)
    
    storage2 = Storage(str(file_path))
    assert storage2.get_task(1).status == Status.COMPLETED
    
def test_load_corrupt_json_returns_empty(tmp_path):
    """write garbage text directly to file, then construct Storage — should not crash"""
    file_path = tmp_path / "tasks.json"
    file_path.write_text("{ garbage data : [ ")
    storage = Storage(str(file_path))
    
    assert len(storage.tasks) == 0