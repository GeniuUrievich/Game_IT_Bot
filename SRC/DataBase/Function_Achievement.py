from sqlalchemy import select
from sqlalchemy.orm import joinedload

from SRC.DataBase.DataBase import Session
from SRC.Models.User import User
from SRC.Models.Achievements import Achievement

async def add_achievement(title_s:str, description_s:str, requirements_s:str):
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

async def add_achiv_user(id:int, title_ac:str):
    async with Session() as session:
        async with session.begin():
            result1 = await session.execute(select(User).options(joinedload(User.achievements)).filter_by(telegram_id=id))
            user = result1.scalars().first()
            result2 = await session.execute(select(Achievement).filter_by(title=title_ac))
            achievement = result2.scalars().first()
            if achievement not in user.achievements and user.task_all_done == int(achievement.requirements):
                user.achievements.append(achievement)
                await session.commit()