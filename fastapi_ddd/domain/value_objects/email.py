class Email:
    def __init__(self, address: str):
        if not self._validate_email(address):
            raise ValueError("Invalid email format")
        self.address = address

    def _validate_email(self, address: str) -> bool:
        return "@" in address  # Basic validation for simplicity
