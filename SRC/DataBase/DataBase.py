
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from SRC.Models.Base_model import Base
from SRC.Models.User import User
from SRC.Models.Achievements import Achievement
from SRC.Models.Level import Level
from SRC.Models.Programming_language import Programming_language
from SRC.Models.Task import Task
from SRC.Models.User_Achievement import Users_Achievement


engine = create_async_engine("postgresql+asyncpg://postgres:123@localhost/Game_IT_Bot", echo=True)

Session = async_sessionmaker(bind=engine, expire_on_commit=False)
async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def drop_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)