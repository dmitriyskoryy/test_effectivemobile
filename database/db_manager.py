import json
import os

path_app = os.pardir


class DBmanager:
    """ Менеджер БД"""

    def __init__(self, path_db: str = f'{path_app}/database/db.txt'):
        self.page = 0
        self.limit = 4
        self.path_db = path_db
        try:
            with open(self.path_db, 'r'):
                pass
        except:
            with open(self.path_db, 'w') as f:
                json_data = json.dumps({})
                f.write(f'{json_data}')

    def _total_record(self) -> int:
        """ Возвращает количество записей в файле (БД)"""
        try:
            with open(self.path_db) as f:
                _dict = json.loads(f.read())
                total_record = len(_dict)
                return total_record
        except Exception as e:
            print(e)

        return 0

    def create_record(self, data: dict) -> str:
        """  Создает запись в файле (БД)"""
        try:
            total_record = self._total_record() + 1
            with open(self.path_db, 'r') as f:
                data_json = json.loads(f.read())
            with open(self.path_db, 'w') as f:
                data_json[f"{total_record}"] = data
                f.write(json.dumps(data_json))
            return "Создана новая запись!"
        except Exception as e:
            print(e)


    def update_record(self, data: dict, update_record_id: int = None) -> str:
        """  Редактирует запись в файле (БД)"""

        try:
            with open(self.path_db, 'r') as f:
                data_json = json.loads(f.read())
            with open(self.path_db, 'w') as f:
                if update_record_id:
                    data_json[f"{update_record_id}"] = data
                    f.write(json.dumps(data_json))
                return f"Запись № {update_record_id} изменена!"
        except Exception as e:
            print(e)

    def _get_records(self) -> list:
        """ Возвращает записи из файла (БД)"""
        try:
            start_row = (self.limit * self.page - self.limit)
            end_row = self.limit * self.page
            with open(self.path_db, 'r') as f:
                data_json = json.loads(f.read())
                items = []
                for item in data_json:
                    items.append((item, data_json.get(f'{item}')))
                return items[start_row:end_row]
        except Exception as e:
            print(e)

    def _max_page(self):
        """ Возвращает максимальное число страниц
        исходя из количества записей в БД и self.limit
        """
        total_record_db = self._total_record()
        mod = total_record_db % self.limit
        if mod != 0:
            max_page = total_record_db / self.limit
        else:
            max_page = total_record_db // self.limit

        return max_page

    def next_page(self):
        """ Возвращает следующую страницу с записями из файла (БД) """
        max_page = self._max_page()
        if max_page > self.page:
            self.page += 1
        records = self._get_records()
        return records

    def prev_page(self):
        """ Возвращает предыдущую страницу с записями из файла (БД)"""
        if self.page > 1:
            self.page -= 1

        records = self._get_records()
        return records
