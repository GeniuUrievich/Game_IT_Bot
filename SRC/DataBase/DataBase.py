from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from SRC.Models.Base_model import Base
from SRC.Models.User import User
from SRC.Models.Achievements import Achievement
from SRC.Models.Level import Level
from SRC.Models.Programming_language import Programming_language
from SRC.Models.Task import Task
from SRC.Models.User_Achievement import Users_Achievement


engine = create_engine("postgresql+psycopg2://postgres:123@localhost/Game_IT_Bot", echo=True)

Session = sessionmaker(bind=engine)
def create_table():
    Base.metadata.create_all(engine)

def drop_table():
    Base.metadata.drop_all(engine)