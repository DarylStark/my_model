import random
import string
from datetime import datetime

from pydantic import BaseModel, Field


class APIToken(BaseModel):
    """ Model for API tokens """

    created: datetime = Field(default_factory=datetime.utcnow)
    expires: datetime = Field(default_factory=datetime.utcnow)
    enabled: bool = True
    title: str = Field(max_length=64)
    token: str | None = Field(
        default=None,
        min_length=32,
        max_length=32,
        regex='^[a-zA-Z0-9]{32}$'
    )

    def set_random_token(self, force: bool = False) -> str:
        """ Method to generate a random token for this API token """

        if self.token is None or force:
            # Generate random token
            characters = string.ascii_letters
            characters += string.digits
            length = random.randint(32, 32)
            random_token = [random.choice(characters)
                            for i in range(0, length)]
            random_token = ''.join(random_token)
            self.token = random_token
            return random_token

        # Token was already set but force wasn't; raise an error
        raise PermissionError('Token is already set')
