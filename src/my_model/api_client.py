"""Module that contains the class for a API clients."""

from datetime import datetime

from sqlmodel import Field

from ._token_object import TokenObject
from .user_scoped_model import UserScopedModel


class APIClient(UserScopedModel, TokenObject):
    """Model for API clients.

    Attributes:
        created: the datetime when this client was created
        expires: the datetime when this client will expire
        enabled: defines it the client is enabled
        app_name: the name for the app
        app_publisher: the name for the publisher of the app
        redirect_url: a URL where the user will be redirected after a token has
            been granted. Can and should be used by web applications.
    """

    created: datetime = Field(default_factory=datetime.utcnow)
    expires: datetime = Field(default_factory=datetime.utcnow)
    enabled: bool = True
    app_name: str = Field(max_length=64)
    app_publisher: str = Field(max_length=64)
    redirect_url: str | None = Field(
        default=None,
        regex='^https?://',
        max_length=1024)
