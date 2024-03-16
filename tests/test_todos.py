import unittest
from ehana import ToDo, create_todo, list_all_todos


class TestEhana(unittest.TestCase):
    def test_create_todo(self):
        # Test case for create_todo
        todo = create_todo("Buy milk", "Buy milk at the store")
        self.assertEqual(todo.title, "Buy milk")
        self.assertEqual(todo.description, "Buy milk at the store")

    def test_list_all_todos(self):
        # Test case for list_all_todos
        todos = list_all_todos()
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0].title, "Buy milk")


if __name__ == "__main__":
    unittest.main()
