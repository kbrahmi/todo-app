from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String, unique=True)

    task_assignees = relationship("Task", back_populates="assignee")


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    assignee_id = Column(Integer, ForeignKey('user.id'))

    # Relation Many-to-One avec la table Utilisateur
    assignee = relationship("Utilisateur", back_populates="taches_assignees")
