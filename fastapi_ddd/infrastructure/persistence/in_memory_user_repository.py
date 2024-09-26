from domain.entities.user import User
from domain.repositories.user_repository import UserRepository
from typing import Optional

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = {}

    def save(self, user: User) -> None:
        self.users[user.id] = user

    def find_by_id(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id, None)
