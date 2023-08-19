import json
import os

path_app = os.pardir


class DBmanager:
    """ Менеджер БД"""

    def __init__(self, path_db: str = f'{path_app}/database/db.txt'):
        self.path_db = path_db
        try:
            with open(self.path_db, 'r'):
                pass
        except:
            with open(self.path_db, 'w') as f:
                json_data = json.dumps({})
                f.write(f'{json_data}')

    def _total_record(self) -> int:
        """Метод возвращает количество записей в файле (БД)"""
        try:
            with open(self.path_db) as f:
                _dict = json.loads(f.read())
                total_record = len(_dict)
                return total_record
        except Exception as e:
            print(e)

        return 0

    def create_record(self, data: dict) -> str:
        """ Метод создания записи в файле (БД)"""

        try:
            total_record = self._total_record() + 1
            with open(self.path_db, 'r') as f:
                data_json = json.loads(f.read())
            with open(self.path_db, 'w') as f:
                data_json[f"{total_record}"] = data
                f.write(json.dumps(data_json))
                return "Record created"
        except Exception as e:
            print(e)

    def update_record(self, data: dict, update_record_id: int = None) -> str:
        """ Метод изменения записи в файле (БД)"""

        try:
            with open(self.path_db, 'r') as f:
                data_json = json.loads(f.read())
            with open(self.path_db, 'w') as f:
                if update_record_id:
                    data_json[f"{update_record_id}"] = data
                    f.write(json.dumps(data_json))
                    return f"Record № {update_record_id} update"
        except Exception as e:
            print(e)

    def get_records(self, page: int = 1, limit: int = 5) -> list:
        try:
            total_record_db = self._total_record()
            max_page = total_record_db // limit
            if max_page >= page:
                start_row = (limit * page - limit) + 1
                end_row = limit * page
                with open(self.path_db, 'r') as f:
                    data_json = json.loads(f.read())
                    items = []
                    for item in data_json:
                        items.append(data_json.get(f'{item}'))
                    return items[start_row:end_row+1]

        except Exception as e:
            print(e)
