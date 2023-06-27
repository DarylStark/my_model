"""Module that contains the class for a API clients."""

from datetime import datetime

from sqlmodel import Field, Relationship

from .token_model import TokenModel


class APIClient(TokenModel, table=True):
    """Model for API clients.

    Attributes:
        created: the datetime when this client was created.
        expires: the datetime when this client will expire.
        enabled: defines it the client is enabled.
        app_name: the name for the app.
        app_publisher: the name for the publisher of the app.
        redirect_url: a URL where the user will be redirected after a token has
            been granted. Can and should be used by web applications.
        user: the user object for the owner.
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

    # Relationships
    user: 'User' = Relationship(back_populates='api_clients')
