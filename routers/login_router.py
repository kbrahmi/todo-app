from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.user_schema import UserBase, UserCreate, UserLogin
from managers.user_management.user_manager import UserManager
from repositories.user_repository import UserRepository
from authentication.token import get_current_user
from database import get_db

router = APIRouter()


@router.post(
    "/register",
    response_model=UserBase,
    summary="Endpoint for registering a new user."
)
async def create_user(user_create: UserCreate, db: Session = Depends(get_db)):
    user_manager = UserManager(UserRepository(db))
    created_user = user_manager.create_user(user_create)
    return created_user


@router.post("/")
async def login_for_access_token(user_login: UserLogin, db: Session = Depends(get_db)):
    user_manager = UserManager(UserRepository(db))
    user = user_manager.authenticate_user(user_login.email, user_login.password)
    access_token = user_manager.generate_access_token(user.email)
    return {"access_token": access_token, "token_type": "bearer"}
