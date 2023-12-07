from fastapi import APIRouter
from typing import List

from schemas.user_schema import UserBase, UserWithTasks, UserUpdate

router = APIRouter()


@router.get("/users/", response_model=List[UserBase])
async def read_users():
    return {"users": ["user 1", "user 2"]}


@router.get("/{id}/tasks", response_model=UserWithTasks)
async def read_user_tasks(id: int):
    return

@router.patch("/{id}", response_model= UserUpdate)
async def update_user(id: int):
    return



