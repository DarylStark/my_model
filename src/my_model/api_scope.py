"""Module that contains the class for a API clients."""

from pydantic import Field
from ._model import Model


class APIScope(Model):
    """Model for API scopes.

    Class attributes:
        module: the module for the API scope
        subject: the subject for the API scope
    """

    module: str = Field(max_length=32)
    subject: str = Field(max_length=32)

    @property
    def full_scope_name(self) -> str:
        """Property for the full scope name.

        Returns:
          The full scope name as string.
        """
        return f'{self.module}.{self.subject}'
