from database.db_manager import DBmanager
from src.display import view, view_row

temp = {
    "firstname": "Petrov",
    "lastname": "Inanov",
    "surname": "Ivanovich",
    "company": "SSDF",
    "phonework": "80001233123",
    "phoneperson": "8823042304"
}



def display():
    while True:
        view()
        view_row(db.get_records(page=1, limit=3))
        print('\n\n\n Введине')
        s = input()
        print(s)
        break


if __name__ == "__main__":
    db = DBmanager()
    display()
    # db.get_record()
    # print(db.create_record(temp))
