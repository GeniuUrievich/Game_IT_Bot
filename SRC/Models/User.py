from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .Base_model import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, nullable=False, unique=True)
    user_name = Column(String)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    task_series = Column(Integer, default=0)
    task_all_done = Column(Integer, default=0)
    best_store = Column(Integer, default=0)
    task = relationship("Task", back_populates="users")
    achievements = relationship("Achievement", secondary="users_achievement", back_populates="users")