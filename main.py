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

if __name__ == "__main__":
    main()
