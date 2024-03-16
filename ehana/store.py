class Store:
    def __init__(self):
        self.items = {}
        self._next_id = 0

    def next_id(self):
        self._next_id += 1
        return self._next_id


todo_store = Store()
