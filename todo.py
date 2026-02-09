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

