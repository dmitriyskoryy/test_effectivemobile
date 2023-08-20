from database.db_manager import DBmanager
from src.display import view, view_row

db = DBmanager()


def record_menu(update: bool = False) -> str:
    """ Меню создания или редактирования записи в файле (БД)"""
    data = {}
    if update:
        s = input("Введите номер записи для редактирования:  ")
        id_update_record_id = s
    s = input("Введите имя:  ")
    data['firstname'] = s
    s = input("Введите фамилию:  ")
    data['lastname'] = s
    s = input("Введите отчество:  ")
    data['surname'] = s
    s = input("Введите компанию:  ")
    data['company'] = s
    s = input("Введите рабочий телефон:  ")
    data['phonework'] = s
    s = input("Введите мобильный телефон:  ")
    data['phoneperson'] = s
    if update:
        result = db.update_record(data, id_update_record_id)
        return result

    result = db.create_record(data)
    return result


def search():
    pass


def run_command(s: str):
    if s == '>':
        view()
        view_row(db.next_page())
    if s == '<':
        view()
        view_row(db.prev_page())
    if s == '+':
        result = record_menu()
        print(result)
    if s == '-':
        result = record_menu(update=True)
        print(result)
    if s == '?':
        search()
    if s == 'q':
        exit()

def menu():
    while True:
        print('\n\n Меню:')
        print('- Добавить запись: +')
        print('- Редактировать запись: -')
        print('- Поиск по базе:   ?')
        print('- Следующая страница: >')
        print('- Придыдущая страница: <')
        print('- Параметры: #')
        print('- Выход: q')
        s = input("Введите команду:  ")
        run_command(s)
        continue


if __name__ == "__main__":
    while True:
        view()
        view_row(db.next_page())
        menu()
        continue
