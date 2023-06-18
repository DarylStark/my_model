"""Module that contains the class for a API clients."""

from datetime import datetime

from sqlmodel import Field

from ._token_object import TokenObject
from .user_scoped_model import UserScopedModel


class APIToken(UserScopedModel, TokenObject):
    """Model for API clients.

    Attributes:
        created: the datetime when this token was created
        expires: the datetime when this token will expire
        enabled: defines it the token is enabled
        title: the title for the token
    """

    created: datetime = Field(default_factory=datetime.utcnow)
    expires: datetime = Field(default_factory=datetime.utcnow)
    enabled: bool = True
    title: str = Field(max_length=64)
