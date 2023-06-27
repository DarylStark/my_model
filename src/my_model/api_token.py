"""Module that contains the class for a API clients."""

from datetime import datetime

from sqlmodel import Field, Relationship

from .token_model import TokenModel


class APIToken(TokenModel, table=True):
    """Model for API clients.

    Attributes:
        created: the datetime when this token was created.
        expires: the datetime when this token will expire.
        enabled: defines it the token is enabled.
        title: the title for the token.
        user: the user object for the owner.
    """

    created: datetime = Field(default_factory=datetime.utcnow)
    expires: datetime = Field(default_factory=datetime.utcnow)
    enabled: bool = True
    title: str = Field(max_length=64)

    # Relationships
    user: 'User' = Relationship(back_populates='api_tokens')
