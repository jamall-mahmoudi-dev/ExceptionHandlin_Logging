class InvalidAgeError(Exception):
    """Raised when age is not between 18 and 100"""
    def __init__(self, age, message="Age must be between 18 and 100"):
        self.age = age
        self.message = message
        super().__init__(self.message)

class UsernameTakenError(Exception):
    """Raised when username already exists in database"""
    pass
