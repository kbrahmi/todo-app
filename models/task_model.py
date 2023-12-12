from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import Base



class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(Enum('Not started', 'In progress', 'Completed'), nullable=False)

    assignee_id = Column(Integer, ForeignKey('user.id'))

    assignee = relationship("User", back_populates="tasks")
