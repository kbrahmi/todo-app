from sqlalchemy.orm import Session
from models.user_model import User
from schemas.user_schema import UserList, UserUpdate, UserCreate
from schemas.task_schema import TaskBase
from typing import List


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

    def update_user(self, user_id: int, user_update: UserUpdate) -> User:
        user = self.db.query(User).filter(User.id == user_id).first()
        if user:
            for key, value in user_update.dict(exclude_unset=True).items():
                setattr(user, key, value)
            self.db.commit()
            self.db.refresh(user)
            return user

    def create_user(self, user_create: UserCreate) -> User:
        user = User(**user_create.dict())
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_tasks_by_id(self, user_id: int) -> List[TaskBase]:
        user = self.db.query(User).filter(User.id == user_id).first()
        if user:
            return [TaskBase.from_orm(task) for task in user.tasks] if user.tasks else []
        return []

