import json
from pathlib import Path
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

    