from domain.entities.user import User
from domain.value_objects.email import Email
from domain.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def update_user_email(self, user_id: int, new_email: str):
        # Retrieve the user from the repository
        user = self.user_repository.find_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        # Create a new Email value object and update the user's email
        email = Email(new_email)
        user.update_email(email)

        # Save the updated user back into the repository
        self.user_repository.save(user)

        return user
