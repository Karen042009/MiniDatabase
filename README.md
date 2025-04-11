# MiniDatabase
def run_interface():
    db = MiniDatabase()

    while True:
        print("\nOptions: add / list / get / update / delete / search / quit")
        command = input("Enter command: ")

        if command == "add":
            try:
                id_ = int(input("ID: "))
                name = input("Name: ")
                age = input("Age: ")
                email = input("Email: ")
                db.add_record({"id": id_, "name": name, "age": age, "email": email})
            except:
                print("Invalid input.")

        elif command == "list":
            for rec in db.list_records():
                print(rec)

        elif command == "get":
            id_ = int(input("Enter ID: "))
            print(db.get_record(id_))

        elif command == "update":
            id_ = int(input("Enter ID: "))
            name = input("New name: ")
            age = input("New age: ")
            email = input("New email: ")
            db.update_record(id_, {"id": id_, "name": name, "age": age, "email": email})

        elif command == "delete":
            id_ = int(input("Enter ID: "))
            db.delete_record(id_)

        elif command == "search":
            name = input("Enter name to search: ")
            results = db.search_by_name(name)
            for r in results:
                print(r)

        elif command == "quit":
            break

        else:
            print("Unknown command.")
