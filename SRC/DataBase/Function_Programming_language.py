from sqlalchemy import select

from SRC.DataBase.DataBase import Session
from SRC.Models.Programming_language import Programming_language

Languages = [
    Programming_language(language="Python"),
    Programming_language(language="JavaScript"),
    Programming_language(language="C#")
]

async def add_language():
    async with Session() as session:
        async with session.begin():
            session.add_all(Languages)
async def get_language(language:str):
    async with Session() as session:
        async with session.begin():
            query = select(Programming_language).filter_by(language=language)
            result = await session.execute(query)
            return result.scalars().first()