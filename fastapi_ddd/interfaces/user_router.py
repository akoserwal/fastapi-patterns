from fastapi import APIRouter, HTTPException
from application.user_use_case import UserUseCase
from infrastructure.persistence.in_memory_user_repository import InMemoryUserRepository

user_router = APIRouter()

# DDD: UserUseCase as the orchestrator of business logic
user_repository = InMemoryUserRepository()
user_use_case = UserUseCase(user_repository=user_repository)

@user_router.post("/")
def create_user(user_id: int, name: str, email: str):
    try:
        user = user_use_case.create_user(user_id=user_id, name=name, email_address=email)
        return {"id": user.id, "name": user.name, "email": user.email.address}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@user_router.get("/{user_id}")
def get_user(user_id: int):
    user = user_use_case.get_user(user_id=user_id)
    if user:
        return {"id": user.id, "name": user.name, "email": user.email.address}
    else:
        raise HTTPException(status_code=404, detail="User not found")
