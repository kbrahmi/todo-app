from repositories.user_repository import UserRepository

class UserManager:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_users(self):
        users = self.user_repository.get_users()
        return users