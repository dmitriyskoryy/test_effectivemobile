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
    """ Поиск по файлу (БД). Ключевые слова вводятся через пробел.
    Возвращаются записи в которых хотя бы по одному полю есть совпадение с ключевым словом"""
    s = input("Введите ключевые слова через пробел:  ")
    _list = s.split(' ')
    result = db.find_records(params=_list)
    view()
    view_row(result)


def change_limit() -> str:
    """ Устанавливает кол-во записей выводимых на экран. Необходимо ввести число."""

    num = input("Введите число записей, которые необходимо отображать на экране (от 1 до 50):  ")
    try:
        limit = db.change_limit(int(num))
        return f"Количество записей отображаемых на странице изменено на {limit}"
    except Exception as e:
        return f"{e}"


def run_command(s: str):
    if s == '>':
        view()
        view_row(db.next_page())
    elif s == '<':
        view()
        view_row(db.prev_page())
    elif s == '+':
        result = record_menu()
        view()
        view_row(db.last_page())
        print('\n\n', result)
    elif s == '-':
        result = record_menu(update=True)
        view()
        view_row(db.last_page())
        print('\n\n', result)
    elif s == '?':
        search()
    elif s == '#':
        result = change_limit()
        view()
        view_row(db.prev_page())
        print('\n\n', result)
    elif s == 'q':
        exit()
    else:
        view()
        view_row(db.prev_page())


def menu():
    while True:
        print('\n\n Меню:')
        print('- Добавить запись: +')
        print('- Редактировать запись: -')
        print('- Поиск по базе:   ?')
        print('- Следующая страница: >')
        print('- Предыдущая страница: <')
        print('- Установить кол-во записей на странице: #')
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
