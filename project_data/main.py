import json


class MiniDatabase:
    def __init__(self, file_name="data.json"):
        self.file_name = file_name

    def add_record(self, record: dict):
        pass

    def get_record(self, record_id: int) -> dict:
        pass

    def update_record(self, record_id: int, new_data: dict):
        pass

    def delete_record(self, record_id: int):
        pass

    def list_records(self) -> list:
        pass
