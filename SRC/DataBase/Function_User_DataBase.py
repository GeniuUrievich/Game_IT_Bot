from SRC.DataBase.DataBase import Session
from SRC.Models.User import User


async def add_user(id: int, name: str):#Добавление нового пользователя
    async with Session() as session:
        async with session.begin():
            new_user = User(telegram_id=id, user_name = name)
            if check_user(id):
                session.add(new_user)


async def check_user(id: int):#Проверка пользователя на нахождение в бд
    async with Session() as session:
        async with session.begin():
            if session.query(User).filter_by(telegram_id=id).first() == None:
                return True
    return False