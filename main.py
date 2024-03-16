from ehana import ToDo, create_todo, list_all_todos


def main():
    print("Welcome to ehana!")
    while True:
        command = input(":")

        if command == "q":
            break

        # Create new todo item
        if command == "n":
            print("Enter title:")
            title = input(":")
            print("Enter description:")
            description = input(":")
            create_todo(title, description)

        # List all todo items
        if command == "l":
            for todo in list_all_todos():
                print(todo)

        # Update a todo item
        if command == "u":
            # TODO: Implement update logic
            # 1. Ask for todo id
            # 2. Show the current title and ask for new title. If the user doesn't want to change the title, just press enter.
            # 3. Show the current description and ask for new description. If the user doesn't want to change the description, just press enter.
            # 4. Show the current status and ask for new status. If the user doesn't want to change the status, just press enter.
            # 5. Update the todo item
            pass

        # Update a todo item status
        if command == "s":
            # TODO: Implement update status logic
            # 1. Ask for todo id
            # 2. Show the current status and ask for new status
            # 3. Update the status
            pass

        # Delete a todo item
        if command == "d":
            # TODO: Implement delete logic
            # 1. Ask for todo id
            # 2. Delete the todo item
            pass

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
