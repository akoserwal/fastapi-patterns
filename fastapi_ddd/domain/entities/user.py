from domain.value_objects.email import Email

class User:
    def __init__(self, user_id: int, name: str, email: Email):
        self.id = user_id
        self.name = name
        self.email = email

    def update_email(self, new_email: Email):
        self.email = new_email
