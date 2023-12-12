from sqlalchemy.orm import Session
from models.user_model import User
from typing import List

from schemas.user_schema import UserList


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_users(self) -> UserList:
        print('users:', self.db.query(User).all())
        return self.db.query(User).all()

    def get_user_by_id(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()

    def delete_user_by_id(self, user_id: int) -> bool:
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            return False
        self.db.delete(user)
        self.db.commit()
        return True

