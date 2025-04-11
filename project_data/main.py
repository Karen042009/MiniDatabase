import json


class MiniDatabase:
    def __init__(self, file_name="data.json"):
        self.file_name = file_name
        self.data = []
        try:
            with open(self.file_name) as file:
                self.data = json.load(file)
        except:
            with open(self.file_name, "w") as file:
                json.dump([], file)

    def _save(self):
        with open(self.file_name, "w") as file_w:
            json.dump(self.data, file_w, indent=4)

    def add_record(self, record: dict):
        for i in self.data:
            if i.get("email") == record.get("email"):
                print("duplicate emails")
                return
        self.data.append(record)
        self._save()

    def get_record(self, record_id: int) -> dict:
        for record in self.data:
            if record.get("id") == record_id:
                return record
        return None

    def update_record(self, record_id: int, new_data: dict):
        for i in range(len(self.data)):
            if self.data[i]["id"] == record_id:
                self.data[i] = new_data
                self._save()
                return

    def delete_record(self, record_id: int):
        for i in range(len(self.data)):
            if self.data[i]["id"] == record_id:
                self.data.pop(i)
                self._save()
                return

    def name(self, name):
        for record in self.data:
            if name.lower() == record.get("name").lower():
                return record

    def list_records(self) -> list:
        return self.data


def run_interface():
    db = MiniDatabase()
    while True:
        print("\nOptions: add / list / get / update / delete / search / quit")
        command = input("Enter command: ")
        if command == "add":  #
            try:
                id_ = int(input("ID: "))
                name = input("Name: ")
                age = input("Age: ")
                email = input("Email: ")
                db.add_record({"id": id_, "name": name, "age": age, "email": email})
            except:
                print("Invalid input.")
        elif command == "list":  #
            for rec in db.list_records():
                print(rec)
        elif command == "get":  #
            id_ = int(input("Enter ID: "))
            print(db.get_record(id_))
        elif command == "update":  #
            id_ = int(input("Enter ID: "))
            name = input("New name: ")
            age = input("New age: ")
            email = input("New email: ")
            db.update_record(id_, {"id": id_, "name": name, "age": age, "email": email})
        elif command == "delete":  #
            id_ = int(input("Enter ID: "))
            db.delete_record(id_)
        elif command == "search":  #
            name = input("Enter name to search: ")
            results = db.search_by_name(name)
            for r in results:
                print(r)
        elif command == "stop":  #
            break


run_interface()
