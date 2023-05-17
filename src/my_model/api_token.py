"""Module that contains the class for a API clients."""

from datetime import datetime

from pydantic import Field

from ._token_object import TokenObject


class APIToken(TokenObject):
    """Model for API clients.

    Class attributes:
        created: the datetime when this token was created
        expires: the datetime when this token will expire
        enabled: defines it the token is enabled
        title: the title for the token
    """

    created: datetime = Field(default_factory=datetime.utcnow)
    expires: datetime = Field(default_factory=datetime.utcnow)
    enabled: bool = True
    title: str = Field(max_length=64)
