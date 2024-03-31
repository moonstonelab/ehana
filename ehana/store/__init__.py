from ..config import config
from .csv import CsvStore
from .sqlite import SqliteStore

if config["DEFAULT"]["store"] == "sqlite":
    todo_store = SqliteStore()
elif config["DEFAULT"]["store"] == "csv":
    todo_store = CsvStore()
else:
    raise ValueError("Invalid store type")