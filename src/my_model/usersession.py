"""Module that contains the class for a API clients."""

from datetime import datetime

from pydantic import Field, validate_arguments
from ._model import Model


class UserSession(Model):
    """Model for User Sessions.

    The usersession model is meant for user session that give a authenticated
    user session.

    Attributes:
        created: the datetime when this usersession was created
        secret: a random generated secret for this usersession
        title: the title for this usersession
        host: the host where this usersession was originated. Can be a IPv4
            address, IPv6 address or even a hostname.
    """

    created: datetime = Field(default_factory=datetime.utcnow)
    secret: str | None = Field(default=None, max_length=64)
    title: str | None = Field(default=None, max_length=128)
    host: str | None = Field(default=None, max_length=128)

    @validate_arguments
    def set_random_secret(
            self,
            min_length: int = 32,
            max_length: int = 64) -> str:
        """Set a random secret for this usersession.

        Args:
            min_length: the minimum length for this secret (default=32)
            max_length: the maximum length for this secret (default=64)

        Returns:
            The generated secret.
        """
        # Create a random secret
        self.secret = self.get_random_string(
            min_length, max_length,
            include_punctation=True)

        # Return the created secret
        return self.secret
