from repositories.task_repository import TaskRepository
from schemas.task_schema import TaskBase, TaskList, TaskCreate, TaskUpdate


class TaskManager:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def get_all_tasks(self) -> TaskList:
        return self.task_repository.get_all_tasks()

    def get_task_by_id(self, task_id: int) -> TaskBase:
        task = self.task_repository.get_task_by_id(task_id)
        return TaskBase.from_orm(task) if task else None

    def create_task(self, task_create: TaskCreate) -> TaskBase:
        created_task = self.task_repository.create_task(task_create)
        return TaskBase.from_orm(created_task) if created_task else None

    def update_task(self, task_id: int, task_update: TaskUpdate) -> TaskBase:
        updated_task = self.task_repository.update_task(task_id, task_update)
        return TaskBase.from_orm(updated_task) if updated_task else None

    def delete_task_by_id(self, task_id: int) -> bool:
        return self.task_repository.delete_task(task_id)
