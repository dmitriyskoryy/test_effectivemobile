def view():
    print("\n" * 100)
    """ Функция вывода в консоль заголовка и шапки"""
    print(' ' * 78, 'ТЕЛЕФОННЫЙ СПРАВОЧНИК')
    print('-' * 184)
    print('| № пп', '|',
          ' ' * 7, 'ФАМИЛИЯ', ' ' * 7, '|',
          ' ' * 10, 'ИМЯ', ' ' * 10, '|',
          ' ' * 7, 'ОТЧЕСТВО', ' ' * 7, '|',
          ' ' * 10, 'КОМПАНИЯ', ' ' * 10, '|',
          ' ' * 4, 'ТЕЛЕФОН (рабочий)', ' ' * 4, '|',
          ' ' * 4, 'ТЕЛЕФОН (мобильный)', ' ' * 4, '|')
    print('-' * 184)


def view_row(data: list):
    """ Функция вывода в консоль строк из БД"""

    for row in data:
        _id = row[0]
        lastname = row[1].get("lastname")
        firstname = row[1].get("firstname")
        surname = row[1].get("surname")
        company = row[1].get("company")
        phonework = row[1].get("phonework")
        phoneperson = row[1].get("phoneperson")

        ind_id = 5 - len(str(_id))
        ind_las = 24 - len(lastname)
        ind_fir = 26 - len(firstname)
        ind_sur = 25 - len(surname)
        ind_com = 31 - len(company)
        ind_phow = 28 - len(phonework)
        print(f'  {_id} ',
              ' ' * ind_id, f'{lastname}',
              ' ' * ind_las, f'{firstname}',
              ' ' * ind_fir, f'{surname}',
              ' ' * ind_sur, f'{company}',
              ' ' * ind_com, f'{phonework}',
              ' ' * ind_phow, f'{phoneperson}')
