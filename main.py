import argparse
from todo import Task, Storage, TodoList

def main():
    parser = argparse.ArgumentParser(description="Simple Todo App")
    parser.add_argument("command", choices=["add", "list", "delete", "complete"], help="Command to run")
    parser.add_argument("--title", help="Task title")
    parser.add_argument("--desc", help="Task description", default="")
    parser.add_argument("--index", type=int, help="Task index")

    args = parser.parse_args()

    storage = Storage()
    todo_list = TodoList(storage)

    if args.command == "add":
        if args.title:
            todo_list.add_task(args.title, args.desc)
        else:
            print("Error: --title is required for adding a task.")

    elif args.command == "list":
        tasks = todo_list.list_tasks()
        if not tasks:
            print("No tasks found.")
        
        for i, task in enumerate(tasks):
            status = "[x]" if task.completed else "[ ]"
            print(f"{i + 1}. {status} {task.title}")

    elif args.command == "delete":
        if args.index is not None:
             todo_list.delete_task(args.index - 1)
        else:
            print("Error: --index required for delete.")

    elif args.command == "complete":
        if args.index is not None:
            todo_list.complete_task(args.index - 1)
        else:
            print("Error: --index required for complete.")

if __name__ == "__main__":
    main()
