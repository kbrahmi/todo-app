from sqlalchemy.orm import Session
from models.task_model import Task
from typing import List
from schemas.task_schema import TaskBase, TaskList


class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_tasks(self) -> TaskList:
        return self.db.query(Task).all()

    def get_task_by_id(self, task_id: int) -> Task:
        return self.db.query(Task).filter(Task.id == task_id).first()
