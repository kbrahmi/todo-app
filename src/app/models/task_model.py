from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    status = Column(Enum('Not started', 'In progress', 'Completed'))

    assignee_id = Column(Integer, ForeignKey('user.id'))

    assignee = relationship("User", back_populates="tasks_assignees")
