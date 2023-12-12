from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.user_schema import UserList
from managers.user_management.user_manager import UserManager
from repositories.user_repository import UserRepository
from database import get_db


router = APIRouter()


@router.get("/", response_model=UserList)
async def get_all_users(db: Session = Depends(get_db)):
    user_manager = UserManager(UserRepository(db))
    users = user_manager.get_all_users()
    return users


@router.get("/{id}/tasks")
async def read_user_tasks():
    return


@router.patch("/{id}")
async def update_user():
    return



