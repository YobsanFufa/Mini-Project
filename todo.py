import json

class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["description"], data["completed"])


class Storage:
    def __init__(self, filename='data.json'):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, 'w') as f:
            # Intentional Error: json is not imported
            json.dump([t.to_dict() for t in tasks], f)

    def load(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return [Task.from_dict(d) for d in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []


class TodoList:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load()

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        self.storage.save(self.tasks)
        print(f"Task '{title}' added.")

    def list_tasks(self):
        return self.tasks

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.storage.save(self.tasks)
            print(f"Task {index + 1} completed.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.storage.save(self.tasks)
            print(f"Task '{removed.title}' deleted.")
        else:
            print("Invalid task index.")

