from sqlalchemy.orm import Session
from schemas.user_schema import UserBase
from database import read_all
from typing import List


class UserRepository:
    def __init__(self, db: Session):
        self.db = db


async def get_users() -> List[UserBase]:
    users_data = read_all("user")
    return [UserBase(**user) for user in users_data]
