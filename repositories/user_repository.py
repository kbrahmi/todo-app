from sqlalchemy.orm import Session
from models.user_model import User
from typing import List


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_users(self) -> List[User]:
        return list(self.db.query(User).all())
