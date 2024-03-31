from .store import todo_store
from .model import ToDo

def create_todo(title, description):
    new_todo = ToDo(todo_store.next_id(), title, description, False)
    todo_store.add_todo(new_todo)
    return todo_store.get_todo(new_todo.id)


def list_all_todos():
    return list(todo_store.load())


def update_todo(id, title, description, status):
    todo_store.update_todo(id, title, description, status)
    return todo_store.get_todo(id)

def update_todo_status(id, status):
    found = todo_store.get_todo(id)
    todo_store.update_todo(found.id, found.title, found.description, status)
    return todo_store.get_todo(id)

def get_todo(id):
    return todo_store.get_todo(id)

def delete_todo(id):
    todo_store.delete_todo(id)
