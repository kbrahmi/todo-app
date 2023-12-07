from pydantic import BaseModel
from enum import Enum, unique
from typing import Optional


@unique
class TaskStatusEnum(str, Enum):
    NOT_STARTED = 'Not started'
    IN_PROGRESS = 'In progress'
    COMPLETED = 'Completed'


class TaskBase(BaseModel):
    id: int
    title: str
    description: str
    status: TaskStatusEnum

    class Config:
        orm_mode = True


class Task(TaskBase):
    assignee_id: int


class TaskUpdate(TaskBase):
    title: Optional[str]
    description: Optional[str]
    status: Optional[TaskStatusEnum]
    assignee_id: Optional[int]
