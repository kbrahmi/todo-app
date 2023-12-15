from pydantic import BaseModel
from enum import Enum, unique
from typing import Optional, List


@unique
class TaskStatusEnum(str, Enum):
    NOT_STARTED = 'Not started'
    IN_PROGRESS = 'In progress'
    COMPLETED = 'Completed'


class TaskBase(BaseModel):
    title: str
    description: str
    status: TaskStatusEnum

    class Config:
        orm_mode = True
        from_attributes = True


class TaskList(BaseModel):
    tasks: List[TaskBase]


class Task(TaskBase):
    assignee_id: int


class TaskUpdate(TaskBase):
    title: Optional[str]
    description: Optional[str]
    status: Optional[TaskStatusEnum]
    assignee_id: Optional[int]


class TaskCreate(BaseModel):
    title: str
    description: str
    status: TaskStatusEnum
    assignee_id: Optional[int] = None

