import argparse
from storage import Storage
from task import Task

def handle_add(args, storage: Storage):
    title = args.title.strip()
    if not title:
        print("Error: title cannot be empty.")
        return
    task = Task(title=title)
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
        

def main():
    parser = argparse.ArgumentParser(prog="devtask")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")
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
    
    args = parser.parse_args()
    storage = Storage()
    
    args.func(args, storage)
    
if __name__ == "__main__":
    main()