from ehana import ToDo, create_todo, list_all_todos, update_todo, get_todo, update_todo_status, delete_todo

def print_all_todos():
    if not list_all_todos():
        print("No todos found.")
        return
    for todo in list_all_todos():
        print(todo)

# I am in branch 1
def main():
    print("Welcome to ehana!")
    print("Enter h for help, q to quit")
    while True:
        command = input(":")

        if command == "q":
            break

        # Create new todo item
        if command == "n":
            print("Enter title:")
            title = input("> ")
            print("Enter description:")
            description = input("> ")
            create_todo(title, description)
            print_all_todos()

        # List all todo items
        if command == "l":
            print_all_todos()

        # Update a todo item
        if command == "u":
            print("Enter todo id:")
            todo_id = input("> ")
            if not todo_id.isdigit() or get_todo(int(todo_id)) is None :
                print("Invalid todo id")
                continue
            print("Enter new title:")
            new_title = input("> ")
            if new_title == "":
                new_title = get_todo(int(todo_id)).title
            print("Enter new description:")
            new_description = input("> ")
            if new_description == "":
                new_description = get_todo(int(todo_id)).description
            print("Is it done? (y/n)")
            is_done = input("> ") == "y"
            update_todo(int(todo_id), new_title, new_description, is_done)
            print_all_todos()

        # Update a todo item status
        if command == "s":
            print("Enter todo id:")
            todo_id = input("> ")
            if not todo_id.isdigit() or get_todo(int(todo_id)) is None :
                print("Invalid todo id")
                continue
            print("Is it done? (y/n)")
            is_done = input("> ") == "y"
            update_todo_status(int(todo_id), is_done)
            print_all_todos()

        # Delete a todo item
        if command == "d":
            print("Enter todo id:")
            todo_id = input("> ")
            found = get_todo(int(todo_id))
            if not todo_id.isdigit() or get_todo(int(todo_id)) is None :
                print("Invalid todo id")
                continue
            delete_todo(int(todo_id))
            print_all_todos()

        # Print help texts
        if command == "h":
            print("Commands:")
            print("  n: Create new todo item")
            print("  l: List all todo items")
            print("  u: Update a todo item")
            print("  s: Update a todo item status")
            print("  d: Delete a todo item")
            print("  q: Quit")

    print("Bye!")


if __name__ == "__main__":
    main()
