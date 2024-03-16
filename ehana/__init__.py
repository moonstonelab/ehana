from .store import todo_store


class ToDo:
    def __init__(self, id, title, description, status):
        self.id = id
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"ID({self.id}) - {self.title} - {self.description} - {'Completed' if self.status else 'Not completed'}"


def create_todo(title, description):
    new_todo = ToDo(todo_store.next_id(), title, description, False)
    todo_store.items[id] = new_todo
    return todo_store.items[id]


def list_all_todos():
    return list(todo_store.items.values())
