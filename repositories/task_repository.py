from sqlalchemy.orm import Session
from models.task_model import Task
from typing import List
from schemas.task_schema import TaskBase, TaskList, TaskCreate, TaskUpdate


class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_tasks(self) -> TaskList:
        return self.db.query(Task).all()

    def get_task_by_id(self, task_id: int) -> Task:
        return self.db.query(Task).filter(Task.id == task_id).first()

    def create_task(self, task_create: TaskCreate) -> Task:
        task = Task(**task_create.dict())
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def update_task(self, task_id: int, task_update: TaskUpdate) -> Task:
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if task:
            for key, value in task_update.dict(exclude_unset=True).items():
                setattr(task, key, value)
            self.db.commit()
            self.db.refresh(task)
            return task

    def delete_task(self, task_id: int):
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if task:
            self.db.delete(task)
            self.db.commit()
            return True


