def view():
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

        ind_las = (24 - len(lastname)) // 2
        ind_fir = (26 - len(firstname)) // 2
        ind_sur = (26 - len(surname)) // 2
        ind_com = (26 - len(company)) // 2
        ind_phow = (30 - len(phonework)) // 2
        ind_phop = (30 - len(phoneperson)) // 2
        print(f'  {_id} ', ' ' * ind_las, f'{lastname}', ' ' * ind_las,
              ' ' * ind_fir, f'{firstname}', ' ' * ind_fir,
              ' ' * ind_sur, f'{surname}', ' ' * ind_sur,
              ' ' * ind_com, f'{company}', ' ' * ind_com,
              ' ' * ind_phow, f'{phonework}', ' ' * ind_phow,
              ' ' * ind_phop, f'{phoneperson}', ' ' * ind_phop)
