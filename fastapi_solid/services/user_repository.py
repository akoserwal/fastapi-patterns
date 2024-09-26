from models.user import User
from typing import List, Optional
from abc import ABC, abstractmethod

# Interface segregation with repository abstraction
class IUserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        pass

    @abstractmethod
    def find_by_id(self, user_id: int) -> Optional[User]:
        pass
    
    @abstractmethod
    def get_next_id(self) -> int:
        pass

# Simple in-memory repository adhering to LSP and OCP
class InMemoryUserRepository(IUserRepository):
    def __init__(self):
        self.users: List[User] = []
        self.next_id = 1

    def save(self, user: User) -> None:
        self.users.append(user)
        self.next_id += 1

    def find_by_id(self, user_id: int) -> Optional[User]:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def get_next_id(self) -> int:
        return self.next_id

