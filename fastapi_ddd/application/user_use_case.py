from domain.repositories.user_repository import UserRepository
from domain.entities.user import User
from domain.value_objects.email import Email

class UserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user_id: int, name: str, email_address: str) -> User:
        email = Email(email_address)
        user = User(user_id=user_id, name=name, email=email)
        self.user_repository.save(user)
        return user

    def get_user(self, user_id: int) -> User:
        return self.user_repository.find_by_id(user_id)
