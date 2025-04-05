from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .Base_model import Base


class Achievement(Base):
    __tablename__ = "achievements"

    id = Column(Integer,primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    requirements = Column(String, nullable=False)
    users = relationship("User", secondary="users_achievement", back_populates="achievements")