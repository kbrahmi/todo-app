from fastapi import APIRouter, Depends
from typing import List
from managers.user_management.user_manager import UserManager
from schemas.user_schema import UserList, UserWithTasks, UserUpdate

router = APIRouter()


@router.get("/", response_model=UserList)
async def read_users(user_manager: UserManager = Depends()) -> UserList:
    return user_manager.get_users()


@router.get("/{id}/tasks", response_model=UserWithTasks)
async def read_user_tasks(id: int):
    return

@router.patch("/{id}", response_model= UserUpdate)
async def update_user(id: int):
    return



