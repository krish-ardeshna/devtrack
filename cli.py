import argparse
import datetime
from storage import Storage
from task import Task
from priority import Priority

def handle_add(args, storage: Storage):
    title = args.title.strip()
    if not title:
        print("Error: title cannot be empty.")
        return
    
    parsed_date = None
    if args.due_date:
        try:
            parsed_date = datetime.date.fromisoformat(args.due_date)
        except ValueError:
            print("Error: Invalid date format. Use YYYY-MM-DD.")
            return
    
    parsed_tags = None
    if args.tags:
        parsed_tags = [t.strip() for t in args.tags.split(",") if t.strip()]
        
    priority_val = Priority(args.priority) if args.priority else None
            
    task = Task(
        title=title,
        repo_link=args.repo_link,
        priority=priority_val,
        tags=parsed_tags,
        due_date=parsed_date    
    )
    storage.add_task(task)
    print(f"Added task {task.id}: {task.title}")

def handle_complete(args, storage: Storage):
    ok = storage.complete_task(args.task_id)
    if ok:
        print(f"Task {args.task_id} marked as completed.")
    else:
        print(f"Task {args.task_id} not found.")
        
def handle_remove(args, storage: Storage):
    ok = storage.delete_task(args.task_id)
    if ok:
        print(f"Task {args.task_id} removed.")
    else:
        print(f"Task {args.task_id} not found.")
        
def handle_list(args, storage):
    tasks = storage.tasks
    if args.status:
        tasks = [t for t in tasks if t.status.value == args.status]
    if not tasks:
        print("No tasks.")
    for t in tasks:
        print(t)
        
def handle_update(args, storage: Storage):
    parsed_date = None
    if args.due_date:
        try:
            parsed_date = datetime.date.fromisoformat(args.due_date)
        except ValueError:
            print("Error: Invalid date format. Use YYYY-MM-DD.")
            return
    
    parsed_tags = None
    if args.tags:
        parsed_tags = [t.strip() for t in args.tags.split(",") if t.strip()]
        
    priority_val = Priority(args.priority) if args.priority else None
    
    ok = storage.update_task(
        args.task_id, 
        title=args.title, 
        repo_link=args.repo_link,
        priority=priority_val,
        tags=parsed_tags,
        due_date=parsed_date
    )
    if ok:
        print(f"Task {args.task_id} updated successfully.")
    else:
        print(f"Task {args.task_id} not found.")

def main():
    parser = argparse.ArgumentParser(prog="devtask")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")
    add_parser.add_argument("--repo-link", default=None)
    add_parser.add_argument("--priority", choices=["low", "medium", "high"], default="medium")
    add_parser.add_argument("--tags", default=None)
    add_parser.add_argument("--due-date", default=None)
    add_parser.set_defaults(func=handle_add)
    
    # complete
    complete_parser = subparsers.add_parser("complete")
    complete_parser.add_argument("task_id", type=int)
    complete_parser.set_defaults(func=handle_complete)
    
    # remove
    remove_parser = subparsers.add_parser("remove")
    remove_parser.add_argument("task_id", type=int)
    remove_parser.set_defaults(func=handle_remove)

    # list
    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("--status", choices=["pending", "completed"], default=None)
    list_parser.set_defaults(func=handle_list)
    
    # update
    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("task_id", type=int)
    update_parser.add_argument("--title", default=None)
    update_parser.add_argument("--repo-link", dest="repo_link", default=None)
    update_parser.add_argument("--priority", choices=["low", "medium", "high"], default=None)
    update_parser.add_argument("--tags", default=None)
    update_parser.add_argument("--due-date", default=None)
    update_parser.set_defaults(func=handle_update)

    args = parser.parse_args()
    storage = Storage()
    
    args.func(args, storage)
    
if __name__ == "__main__":
    main()