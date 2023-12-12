from repositories.user_repository import UserRepository
from schemas.user_schema import UserList, UserBase


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

