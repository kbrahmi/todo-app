from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user_schema import UserBase, UserList, UserUpdate, UserCreate
from managers.user_management.user_manager import UserManager
from repositories.user_repository import UserRepository
from database import get_db


router = APIRouter()


@router.get("/", response_model=UserList)
async def get_all_users(db: Session = Depends(get_db)):
    user_manager = UserManager(UserRepository(db))
    users = user_manager.get_all_users()
    return UserList(users=[UserBase.from_orm(user) for user in users])


@router.get("/{id}", response_model=UserBase)
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user_manager = UserManager(UserRepository(db))
    user = user_manager.get_user_by_id(user_id)
    return user


@router.get("/{id}/tasks")
async def read_user_tasks():
    return


@router.patch("/{id}", response_model=UserBase)
async def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    user_manager = UserManager(UserRepository(db))
    updated_user = user_manager.update_user(user_id, user_update)
    return updated_user


@router.delete("/{id}")
async def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user_manager = UserManager(UserRepository(db))
    user_manager.delete_user_by_id(user_id)
    return {"message": "User deleted successfully"}


@router.post("/", response_model=UserBase)
async def create_user(user_create: UserCreate, db: Session = Depends(get_db)):
    user_manager = UserManager(UserRepository(db))
    created_user = user_manager.create_user(user_create)
    return created_user
