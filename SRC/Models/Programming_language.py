from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .Base_model import Base


class Programming_language(Base):
    __tablename__ = "programming_languages"

    id = Column(Integer, primary_key=True)
    language = Column(String)
    tasks = relationship("Task", back_populates="prog_language")