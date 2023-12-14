from pydantic import BaseModel, EmailStr
from typing import List, Optional
from schemas.task_schema import TaskBase


class UserBase(BaseModel):
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
        from_attributes = True


class UserName(BaseModel):
    name: str

    class Config:
        orm_mode = True
        from_attributes = True


class UserList(BaseModel):
    users: List[UserBase]


class UserUpdate(UserBase):
    name: Optional[str]
    password: Optional[str]
    email: Optional[EmailStr]

    class Config:
        orm_mode = True
        from_attributes = True


class UserCreate(BaseModel):
    name: str
    password: str
    email: EmailStr

    class Config:
        orm_mode = True
        from_attributes = True


class UserTasks(BaseModel):
    user: UserName
    tasks: List[TaskBase]

    class Config:
        orm_mode = True
        from_attributes = True





