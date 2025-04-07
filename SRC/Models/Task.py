from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .Base_model import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    condition = Column(String, nullable=False)
    answer = Column(Integer, nullable=False)
    attemp_all = Column(Integer, default=0)
    attemp_true = Column(Integer, default=0)
    level_id = Column(Integer, ForeignKey("levels.id"), nullable=False)
    programming_language_id = Column(Integer, ForeignKey("programming_languages.id"), nullable=False)
    users = relationship("User", back_populates="task")
    level = relationship("Level", back_populates="tasks")
    prog_language = relationship("Programming_language", back_populates="tasks")