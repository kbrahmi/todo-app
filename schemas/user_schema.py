from pydantic import BaseModel, EmailStr
from typing import List
from typing import Optional
from models.task_model import Task as TaskModel


class UserBase(BaseModel):
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
        from_attributes = True


class UserList(BaseModel):
    users: List[UserBase]


# class UserWithTasks(UserBase):
#    tasks: List[Task] = []


class UserUpdate(UserBase):
    name: Optional[str]
    email: Optional[str]

