from pydantic import BaseModel, EmailStr
from typing import List
from typing import Optional
from .task_schema import Task


class UserBase(BaseModel):
    name: str
    email: EmailStr

    class Config:
        orm_mode = True


class UserList(BaseModel):
    users: List[UserBase]


# class UserWithTasks(UserBase):
#    tasks: List[Task] = []


class UserUpdate(UserBase):
    name: Optional[str]
    email: Optional[str]

