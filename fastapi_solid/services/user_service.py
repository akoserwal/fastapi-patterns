from schemas.user_schema import CreateUserRequest, UserResponse
from models.user import User
from services.user_repository import IUserRepository

class UserService:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def create_user(self, user_data: CreateUserRequest) -> UserResponse:
        user = User(id=self.user_repository.get_next_id(), name=user_data.name, email=user_data.email)
        self.user_repository.save(user)
        return UserResponse(id=user.id, name=user.name, email=user.email)
    
    def get_user(self, user_id: int) -> UserResponse:
        user = self.user_repository.find_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return UserResponse(id=user.id, name=user.name, email=user.email)
