from sqlalchemy import select

from SRC.DataBase.DataBase import Session
from SRC.Models.Level import Level

Levels = [
    Level(title="Новичок", description="Только начал изучение. Осваиваешь основы — переменные, типы данных, простые команды."),
    Level(title="Ученик", description="Уже понимаешь, как писать простые программы. Работаешь с циклами, условиями, функциями."),
    Level(title="Продвинутый", description="Пишешь собственные проекты, знаком с ООП, базами данных и асинхронностью."),
    Level(title="Разработчик", description="Уверенно проектируешь архитектуру, работаешь с фреймворками, знаешь, как строить приложения."),
    Level(title="Мастер", description="Не просто пишешь код — ты создаёшь системы. Настраиваешь автоматизацию, обучаешь других и ведёшь проекты")
]
async def add_level():
    async with Session() as session:
        async with session.begin():
            session.add_all(Levels)

async def get_level(title: str):
    async with Session() as session:
        async with session.begin():
            query = select(Level).filter_by(title=title)
            result = await session.execute(query)
            return result.scalars().first()
