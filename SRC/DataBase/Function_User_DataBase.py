import random

from sqlalchemy import select, desc
from sqlalchemy.orm import selectinload

from SRC.DataBase.DataBase import Session
from SRC.DataBase.Function_Achievement import add_achiv_user
from SRC.DataBase.Function_Level import get_level
from SRC.DataBase.Function_Programming_language import get_language
from SRC.DataBase.Function_Task import get_text_task
from SRC.Models.Achievements import Achievement
from SRC.Models.User import User
from SRC.Models.Task import Task


async def add_user(id_teleg: int, name: str):#Добавление нового пользователя
    async with Session() as session:
        async with session.begin():
            new_user = User(telegram_id=id_teleg, user_name = name)
            if await check_user(id_teleg):
                session.add(new_user)


async def check_user(id_teleg: int):#Проверка пользователя на нахождение в бд
    async with Session() as session:
        async with session.begin():
            query = select(User).filter_by(telegram_id=id_teleg)
            result = await session.execute(query)
            if result.scalars().first != None:
                return True
    return False

async def true_answer_task(id_teleg: int):
    async with Session() as session:
        async with session.begin():
            query = select(User).filter_by(telegram_id=id_teleg)
            result = await session.execute(query)
            user = result.scalars().first()
            user.task_series += 1
            user.task_all_done += 1
            if user.task_series > user.best_store:
                user.best_store = user.task_series
            result2 = await session.execute(select(Task).filter_by(id=user.task_id))
            task = result2.scalars().first()
            task.attemp_all += 1
            task.attemp_true += 1
    return await check_requirements(id_teleg)
async def false_answer_task(id_teleg: int):
    async with Session() as session:
        async with session.begin():
            query = select(User).filter_by(telegram_id=id_teleg)
            result = await session.execute(query)
            user = result.scalars().first()
            user.task_series = 0
            result2 = await session.execute(select(Task).filter_by(id=user.task_id))
            task = result2.scalars().first()
            task.attemp_all += 1
            task.attemp_true += 1

async def issue_task(id_teleg: int, lang:str, lev: str):
    level = await get_level(lev)
    language = await get_language(lang)
    async with Session() as session:
        async with session.begin():
            query = select(User).filter_by(telegram_id=id_teleg)
            result = await session.execute(query)
            user = result.scalars().first()
            query_2 = select(Task).filter_by(level_id=level.id, programming_language_id=language.id)
            result_2 = await session.execute(query_2)
            tasks = result_2.scalars().all()
            task_user = random.choice(tasks)
            user.task_id = task_user.id
            text = await get_text_task(task_user.id)
    return text

async def get_user(id_teleg: int):
    async with Session() as session:
        async with session.begin():
            query = select(User).filter_by(telegram_id=id_teleg)
            result = await session.execute(query)
            user = result.scalars().first()
    return user

async def get_user_sortded_bs():
    top_3_user = []
    async with Session() as session:
        async with session.begin():
            result = await session.execute(select(User).order_by(desc(User.best_store)))
            users = result.scalars().all()
            for i in range(2):
                top_3_user.append(users[i])
    return top_3_user

async def check_requirements(id_user:int):
    async with Session() as session:
        async with session.begin():
            result = await session.execute((select(Achievement.title,Achievement.requirements)))
            result1 = await session.execute(select(User).filter_by(telegram_id=id_user))
            achivs = result.all()
            user = result1.scalars().first()
    s = ""
    for achiv in achivs:
        if user.task_all_done >= int(achiv[1]):
            if await add_achiv_user(id_user,achiv[0]):
                s += f"Поздравляем!!! Вы получили достижение {achiv[0]} за {achiv[1]} верных ответов.\n"
    return s

async def get_achievement(id_user:int):
    s = "Ваши достижения:\n"
    async with Session() as session:
        async with session.begin():
            result = await session.execute(select(User).where(User.telegram_id == id_user).options(selectinload(User.achievements)))
            user = result.scalars().first()
    for i in range(len(user.achievements)):
        s += f"{i+1}. {user.achievements[i].title} за условие: {user.achievements[i].description}\n"
    return s