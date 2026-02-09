# Mini Project: OOP-Based Todo App

A robust command-line Todo application built with Python. This project demonstrates Object-Oriented Programming (OOP) principles and data persistence using JSON.

## Features

- **Add Tasks**: Create new tasks with title and description.
- **List Tasks**: View all tasks with their completion status.
- **Complete Tasks**: Mark tasks as done.
- **Delete Tasks**: Remove tasks from the list.
- **Data Persistence**: Tasks are saved to `data.json` automatically.

## Project Structure

- `main.py`: The entry point for the CLI application. Handles user arguments and commands.
- `todo.py`: Contains the core logic and classes:
  - `Task`: Represents a single task (Model).
  - `TodoList`: Manages the collection of tasks (Controller).
  - `Storage`: Handles reading from and writing to the JSON file.
- `data.json`: Stores the task data (created automatically).

## Setup and Installation

### Prerequisites

- Python 3.x installed.

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

## Usage

Run the application using `python main.py`.

### Add a Task

```bash
python main.py add --title "STUDY DJANGO" --desc "Study django today for 2 hr "
```

### List Tasks

```bash
python main.py list
```

### Complete a Task

```bash
python main.py complete --index 1
```

_Note: The command uses a 1-based index (e.g., use 1 for the first task) for user convenience._

### Delete a Task

```bash
python main.py delete --index 1
```

## JSON <-> Object Conversion

This project creates a seamless bridge between Python objects and JSON data for storage.

### Serialization (Object to JSON)

The `Task` class includes a `to_dict()` instance method that converts a `Task` object into a standard Python dictionary.

```python
def to_dict(self):
    return {
        "title": self.title,
        "description": self.description,
        "completed": self.completed
    }
```

The `Storage` class then uses `json.dump()` to serialize this list of dictionaries into the `data.json` file.

### Deserialization (JSON to Object)

When loading data, the `Storage` class reads the JSON file using `json.load()`, which returns a list of dictionaries. The `Task` class provides a `from_dict()` class method to verify and convert each dictionary back into a full `Task` object.

```python
@classmethod
def from_dict(cls, data):
    return cls(data["title"], data["description"], data["completed"])
```
