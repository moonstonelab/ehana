import os
import csv
from .model import ToDo

# Define the file path
file_path = "store.csv"


class Store:
    def __init__(self):
        """
        Initializes a new store.
        """
        self.items = {}
        self._next_id = 0

        # Check if the file exists
        if not os.path.exists(file_path):
            # Create an empty file if it doesn't exist
            with open(file_path, "w", newline="") as file:
                pass  # Empty pass statement to create the file
            print(f"File '{file_path}' created successfully!")

        # Now try to read the file
        try:
            with open(file_path, "r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    # Assuming header row has column names matching class attributes
                    id = int(row["id"])
                    if self._next_id <= id:
                        self._next_id = id
                    todo = ToDo(
                        id,
                        row["title"],
                        row["description"],
                        True if row["status"] == "True" else False,
                    )
                    self.items[todo.id] = todo
        except FileNotFoundError:
            print(f"Error: Could not find file '{file_path}'.")
        except KeyError as e:
            print(f"Error: Missing column name '{e.args[0]}' in the CSV file.")

    def next_id(self):
        self._next_id += 1
        return self._next_id

    def save(self):
        """
        Saves the store to the CSV file.
        """
        with open(file_path, "w", newline="") as csvfile:
            fieldnames = ["id", "title", "description", "status"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for todo in self.items.values():
                writer.writerow(
                    {
                        "id": todo.id,
                        "title": todo.title,
                        "description": todo.description,
                        "status": "True" if todo.status else "False",
                    }
                )


todo_store = Store()
