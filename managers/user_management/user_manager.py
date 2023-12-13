from repositories.user_repository import UserRepository
from schemas.user_schema import UserList, UserBase, UserUpdate, UserCreate


class UserManager:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_all_users(self) -> UserList:
        return self.user_repository.get_all_users()

    def get_user_by_id(self, user_id: int) -> UserBase:
        user = self.user_repository.get_user_by_id(user_id)
        return UserBase.from_orm(user) if user else None

    def delete_user_by_id(self, user_id: int) -> bool:
        return self.user_repository.delete_user_by_id(user_id)

    def update_user(self, user_id: int, user_update: UserUpdate) -> UserBase:
        updated_user = self.user_repository.update_user(user_id, user_update)
        return UserBase.from_orm(updated_user) if updated_user else None

    def create_user(self, user_create: UserCreate) -> UserBase:
        created_user = self.user_repository.create_user(user_create)
        return UserBase.from_orm(created_user) if created_user else None
