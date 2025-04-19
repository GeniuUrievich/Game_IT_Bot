from sqlalchemy import select

from SRC.DataBase.DataBase import Session
from SRC.Models import User
from SRC.Models.Achievements import Achievement

async def add_achievenent(title_s:str, description_s:str, requirements_s:str):
    async with Session() as session:
        new_achievement = Achievement(title=title_s, description=description_s, requirements=requirements_s)
        async with session.begin():
            if await check_achievement(title_s):
                session.add(new_achievement)


async def check_achievement(title_ach: str):#Проверка достижения на нахождение в бд
    async with Session() as session:
        async with session.begin():
            query = select(Achievement).filter_by(title=title_ach)
            result = await session.execute(query)
            if result.scalars().first() == None:
                return True
    return False

async def check_ach_user(telegr_id:int, title_ach: str):
    async with Session() as session:
        async with session.begin():
            query1 = select(User).filter_by(teleg_id=telegr_id)
            query2 = select(Achievement).filter_by(title=title_ach)
            result1 = await session.execute(query1)
            result2 = await session.execute(query2)
            user = result1.scalars().first()
            achievement = result2.scalars().first()
            if achievement not in user.achievements:
                return True
    return False