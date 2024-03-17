class ToDo:
    def __init__(self, id, title, description, status):
        self.id = id
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"ID({self.id}) - {self.title} - {self.description} - {'Completed' if self.status else 'Not completed'}"
