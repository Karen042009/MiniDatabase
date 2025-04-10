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
                return  #  թե ավելի լավա break

    def list_records(self) -> list:
        return self.data


mini = MiniDatabase()
record_1 = {"id": 1, "name": "Karen", "age": 15, "email": "karenpoghosyan@gmail.com"}
mini.add_record(record_1)
record_2 = {"id": 2, "name": "Anna", "age": "+-12", "email": "ani47556@gmail.com"}
mini.add_record(record_2)
mini.delete_record(2)
print(mini.list_records())
