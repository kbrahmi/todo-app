from pydantic import BaseModel
from enum import Enum as PyEnum


class TaskStatusEnum(str, PyEnum):
    NOT_STARTED = 'Not started'
    IN_PROGRESS = 'In progress'
    COMPLETED = 'Completed'


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: TaskStatusEnum

