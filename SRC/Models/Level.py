from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .Base_model import Base


class Level(Base):
    __tablename__ = "levels"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    tasks = relationship("Task", back_populates="level")