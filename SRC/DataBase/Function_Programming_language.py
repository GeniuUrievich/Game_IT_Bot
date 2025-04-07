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
