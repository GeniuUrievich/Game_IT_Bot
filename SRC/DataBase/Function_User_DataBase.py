from SRC.DataBase.DataBase import Session
from SRC.Models.User import User


def add_user(id: int, name: str):#Добавление нового пользователя
    session = Session()
    new_user = User(telegram_id=id, user_name = name)
    if check_user(id):
        session.add(new_user)
        session.commit()
    session.close()

def check_user(id: int):#Проверка пользователя на нахождение в бд
    session = Session()
    if session.query(User).filter_by(telegram_id=id).first() == None:
        return True
    return False