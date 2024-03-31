from .store import todo_store
from .model import ToDo

def create_todo(title, description):
    new_todo = ToDo(todo_store.next_id(), title, description, False)
    todo_store.items[new_todo.id] = new_todo
    todo_store.save()
    return todo_store.items[new_todo.id]


def list_all_todos():
    return list(todo_store.items.values())


def update_todo(id, title, description, status):
    todo_store.items[id].title = title
    todo_store.items[id].description = description
    todo_store.items[id].status = status
    todo_store.save()
    return todo_store.items[id]

def update_todo_status(id, status):
    todo_store.items[id].status = status
    todo_store.save()
    return todo_store.items[id]

def get_todo(id):
    return todo_store.items.get(id)

def delete_todo(id):
    del todo_store.items[id]
    todo_store.save()
    if len(todo_store.items) == 0:
        todo_store.reset_next_id()