from repositories.user_repository import UserRepository
from models.user_model import User
from typing import List


class UserManager:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_all_users(self) -> List[User]:
        return self.user_repository.get_all_users()
