from .store import todo_store
from .model import ToDo

def create_todo(title, description):
    new_todo = ToDo(todo_store.next_id(), title, description, False)
    todo_store.items[id] = new_todo
    todo_store.save()
    return todo_store.items[id]


def list_all_todos():
    return list(todo_store.items.values())
