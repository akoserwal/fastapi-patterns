from fastapi import APIRouter, Depends, HTTPException
from schemas.user_schema import CreateUserRequest, UserResponse
from services.user_service import UserService
from services.user_repository import InMemoryUserRepository

user_router = APIRouter()

# Dependency inversion with UserService depending on repository abstraction
user_service = UserService(user_repository=InMemoryUserRepository())

@user_router.post("/", response_model=UserResponse)
def create_user(user_data: CreateUserRequest):
    try:
        return user_service.create_user(user_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@user_router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    try:
        return user_service.get_user(user_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="User not found")
