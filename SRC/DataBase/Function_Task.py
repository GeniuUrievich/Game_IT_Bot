from sqlalchemy import select

from SRC.DataBase.DataBase import Session
from SRC.DataBase.Function_Level import get_level
from SRC.DataBase.Function_Programming_language import get_language
from SRC.Models.Task import Task

async def add_task(condition: str, answer:str, level_title:str, prog_language:str):
    level = await get_level(level_title)
    language = await get_language(prog_language)
    if not level and not language:
        print("Ошибка")
        return

    new_task = Task(
        condition=condition,
        answer=answer,
        level_id=level.id,
        programming_language_id=language.id
    )
    async with Session() as session:
        async with session.begin():
            session.add(new_task)

async def check_answer(id_task: int, answer: str):
    answer_int = int(answer)
    async with Session() as session:
        async with session.begin():
            query = select(Task).filter_by(id=id_task)
            result = await session.execute(query)
            task = result.scalars().first()
            if task.answer == answer_int:
                return True
            else:
                return False
