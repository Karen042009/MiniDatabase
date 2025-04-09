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

    def add_record(self, record: dict):
        self.data.append(record)
        with open(self.file_name, "w") as file_w:
            json.dump(self.data, file_w, indent=4)  #

    def get_record(self, record_id: int) -> dict:
        pass

    def update_record(self, record_id: int, new_data: dict):
        pass

    def delete_record(self, record_id: int):
        pass
    def list_records(self) -> list:
        pass
    
    
db = MiniDatabase()
record_1 = {"id": 1, "name": "Karen", "age": 16, "email": "karen@example.com"}
db.add_record(record_1)
record_2 = {"id": 2, "name": "Anna", "age": 18, "email": "anna@example.com"}
db.add_record(record_2)