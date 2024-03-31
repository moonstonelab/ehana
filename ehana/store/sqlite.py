import sqlite3
from ..model import ToDo
from ..config import config

# Define the file path
db_file = config["DEFAULT"]["sqlitefile"]


class SqliteStore:
    def __init__(self):

        self.conn = sqlite3.connect(db_file)
        cursor = self.conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS todo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                description TEXT,
                status INTEGER
            )
            """
        )
        self.conn.commit()

    def next_id(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(id) FROM todo")
        row = cursor.fetchone()
        return (row[0] or 0) + 1

    def reset_next_id(self):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM todo")
        self.conn.commit()

    def save(self, todo):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO todo (title, description, status) VALUES (?, ?, ?)",
            (todo.title, todo.description, todo.status),
        )
        self.conn.commit()

    def load(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM todo")
        return [
            ToDo(
                id,
                title,
                description,
                status,
            )
            for id, title, description, status in cursor.fetchall()
        ]

    def add_todo(self, todo):
        self.save(todo)

    def get_todo(self, id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM todo WHERE id =?", (id,))
        row = cursor.fetchone()
        if row is None:
            return None
        return ToDo(
            row[0],
            row[1],
            row[2],
            row[3],
        )

    def update_todo(self, id, title, description, status):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE todo SET title =?, description =?, status =? WHERE id =?",
            (title, description, status, id),
        )
        self.conn.commit()

    def delete_todo(self, id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM todo WHERE id =?", (id,))
        self.conn.commit()
