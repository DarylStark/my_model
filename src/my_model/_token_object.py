"""Module that contains the base class for models that have a token."""

from pydantic import validate_arguments
from sqlmodel import Field

from ._model import Model


class TokenObject(Model):
    """Basemodel for classes that use tokens.

    Defines the `set_random_token` method that can and should be used to
    generate a random token.

    Attributes:
        token: the token for the object
    """

    token: str | None = Field(
        default=None,
        min_length=32,
        max_length=32,
        regex='^[a-zA-Z0-9]{32}$'
    )

    @validate_arguments
    def set_random_token(self, force: bool = False) -> str:
        """Set a random generated token.

        Args:
            force: if set to True, the token will be generated even if None is
                set. If set to False, a token will only be set if there is no
                token already set.

        Returns:
            A string with the token that is set.

        Raises:
            PermissionError: a token was already set and `force` was not set to
            True.
        """
        if self.token is None or force:
            # Generate random token
            self.token = self.get_random_string(
                min_length=32,
                max_length=32,
                include_punctation=False)

            return self.token

        # Token was already set but force wasn't; raise an error
        raise PermissionError('Token is already set')
