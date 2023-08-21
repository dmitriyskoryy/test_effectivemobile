import json
import math

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class DBmanager:
    """ Менеджер БД"""

    def __init__(self, path_db: str = f'{BASE_DIR}/db.txt'):
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
            return f'{e}'

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
            return f'{e}'

    def _get_records(self) -> list:
        """ Возвращает записи из файла (БД)"""
        try:
            start_row = (self.limit * self.page - self.limit)
            end_row = self.limit * self.page
            with open(self.path_db, 'r') as f:
                data_json = json.loads(f.read())
                _list = []
                for row in data_json:
                    _list.append((row, data_json.get(row)))
                return _list[start_row:end_row]
        except Exception as e:
            print(e)

    def _max_page(self):
        """ Возвращает максимальное число страниц
        исходя из количества записей в БД и self.limit
        """
        total_record_db = self._total_record()
        if total_record_db <= 1:
            return 1
        mod = total_record_db % self.limit
        if mod != 0:
            max_page = total_record_db / self.limit
        else:
            max_page = total_record_db // self.limit

        return math.ceil(max_page)

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

    def last_page(self):
        """ Возвращает последнюю страницу с записями из файла (БД)"""
        self.page = self._max_page()
        records = self._get_records()
        return records

    def find_records(self, params: list) -> list:
        """ Поиск записей по заданным параметрам """

        with open(self.path_db, 'r') as f:
            data_json = json.loads(f.read())
            _list = []
            for param in params:
                for row in data_json:
                    if param in data_json.get(row).values():
                        _list.append((row, data_json.get(row)))

            return _list

    def change_limit(self, limit: int = 4) -> int:
        """ Устанавливает кол-во (self.limit) записей выводимых на странице.
        Число не должно быть больше 50"""
        if limit < 1 or limit > 50:
            self.limit = 4
        else:
            self.limit = limit

        return self.limit
