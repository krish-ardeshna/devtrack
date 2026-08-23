import json
from pathlib import Path
import copy
from task import Task

class Storage:
    def __init__(self, file_path: str = "tasks.json"):
        self.file_path = Path(file_path)
        self.tasks = self._load()
        
    def _load(self):
        if not self.file_path.exists():
            return []

        try:
            content = self.file_path.read_text()
        except OSError as e:
            print(f"Warning: Could not read {self.file_path} ({e}). Starting with empty task list.")
            return []

        if not content.strip():
            return []

        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            print(f"Warning: Could not parse {self.file_path}. Starting with empty task list.")
            return []

        return [Task.from_dict(task) for task in data]
    
    def _save(self):
        try:
            data = [task.to_dict() for task in self.tasks]
            content = json.dumps(data, indent=2)
            tmp_path = self.file_path.with_suffix(".tmp")
            tmp_path.write_text(content)
            tmp_path.replace(self.file_path)
        except OSError as e:
            print(f"Error: Could not save tasks to {self.file_path} ({e}).")

    def _next_id(self) -> int:
        if not self.tasks:
            return 1
        return max(task.id for task in self.tasks) + 1
                    
    def add_task(self, task: Task):
        task.id = self._next_id()
        self.tasks.append(task)
        self._save()
        
    def _find_task(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_task(self, task_id: int):
        task = self._find_task(task_id)
        return copy.deepcopy(task) if task else None

    def update_task(
        self,
        task_id: int,
        title: str | None = None,
        repo_link: str | None = None,
    ) -> bool:
        task = self._find_task(task_id)
        if task is None:
            return False

        changed = False
        if title is not None:
            task.title = title
            changed = True
        if repo_link is not None:
            task.repo_link = repo_link
            changed = True

        if changed:
            self._save()
        return True
    
    def delete_task(self, task_id: int):
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                self._save()
                return True
        return False
    
    def complete_task(self, task_id: int) -> bool:
        task = self._find_task(task_id)
        if task is None:
            return False
        task.complete()
        self._save()
        return True