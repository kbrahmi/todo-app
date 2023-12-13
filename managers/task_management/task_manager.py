from repositories.task_repository import TaskRepository
from schemas.task_schema import TaskBase, TaskList
from sqlalchemy.orm import Session
from typing import List


class TaskManager:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def get_all_tasks(self) -> TaskList:
        return self.task_repository.get_all_tasks()

    def get_task_by_id(self, task_id: int) -> TaskBase:
        task = self.task_repository.get_task_by_id(task_id)
        return TaskBase.from_orm(task) if task else None

    def create_task(self, task):
        pass

    def update_task(self, task_id: int, updated_task):
        pass

    def delete_task(self, task_id: int):
        pass
