import random

from sqlalchemy import select

from SRC.DataBase.DataBase import Session
from SRC.DataBase.Function_Level import get_level
from SRC.DataBase.Function_Programming_language import get_language
from SRC.DataBase.Function_Task import get_text_task
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

async def false_answer_task(id_teleg: int):
    async with Session() as session:
        async with session.begin():
            query = select(User).filter_by(telegram_id=id_teleg)
            result = await session.execute(query)
            user = result.scalars().first()
            user.task_series = 0

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