
def view():
    """ Функция вывода в консоль заголовка и шапки"""
    print(' ' * 78, 'ТЕЛЕФОННЫЙ СПРАВОЧНИК')
    print('   ', '-' * 177)
    print('   ', '|', ' ' * 7, 'ФАМИЛИЯ', ' ' * 7, '|',
          ' ' * 10, 'ИМЯ', ' ' * 10, '|',
          ' ' * 7, 'ОТЧЕСТВО', ' ' * 7, '|',
          ' ' * 10, 'КОМПАНИЯ', ' ' * 10, '|',
          ' ' * 4, 'ТЕЛЕФОН (рабочий)', ' ' * 4, '|',
          ' ' * 4, 'ТЕЛЕФОН (мобильный)', ' ' * 4, '|')
    print('   ', '-' * 177)



def indent_size(value: str):
    return (25 - len(value)) // 2

def view_row(data: list):
    """ Функция вывода в консоль строк из БД"""

    for row in data:
        lastname = row.get("lastname")
        firstname = row.get("firstname")
        surname = row.get("surname")
        company = row.get("company")
        phonework = row.get("phonework")
        phoneperson = row.get("phoneperson")

        ind_las = (22- len(lastname)) // 2
        ind_fir = (22 - len(firstname)) // 2
        ind_sur = (24 - len(surname)) // 2
        ind_com = (26 - len(company)) // 2
        ind_phow = (28 - len(phonework)) // 2
        ind_phop = (26 - len(phoneperson)) // 2
        print('   ', '|', ' ' * ind_las, f'{lastname}', ' ' * ind_las, '|',
              ' ' * ind_fir, f'{firstname}', ' ' * ind_fir, '|',
              ' ' * ind_sur, f'{surname}', ' ' * ind_sur, '|',
              ' ' * ind_com, f'{company}', ' ' * ind_com, '|',
              ' ' * ind_phow, f'{phonework}', ' ' * ind_phow, '|',
              ' ' * ind_phop, f'{phoneperson}', ' ' * ind_phop, '|')

