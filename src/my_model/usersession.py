from datetime import datetime
from pydantic import BaseModel, Field
import random
import string


class UserSession(BaseModel):
    """ The usersession model is meant for user session that give a
        authenticated user session. """

    created: datetime = Field(default_factory=datetime.utcnow)
    secret: str | None = Field(default=None, max_length=64)
    title: str | None = Field(default=None, max_length=128)
    host: str | None = Field(default=None, max_length=128)

    class Config:
        validate_assignment = True

    def set_random_secret(
            self,
            min_length: int = 32,
            max_length: int = 64) -> str:
        """ Method to set a random secret for the usersession """

        # Generate a random password for this user
        characters = string.ascii_letters
        characters += string.digits
        characters += string.punctuation
        length = random.randint(min_length, max_length)
        random_secret = [random.choice(characters)
                         for i in range(0, length)]
        random_secret = ''.join(random_secret)

        # Set the password for the user
        self.secret = random_secret

        # Return the created password
        return random_secret
