from SRC.DataBase.DataBase import Session
from SRC.Models.User import User


def add_user():
    session = Session()
    new_user = User(telegram_id=1, user_name = "Test")
    session.add(new_user)
    session.commit()
    session.close()