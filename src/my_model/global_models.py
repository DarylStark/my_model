"""Module that contains the classes for global models.

These models are _not_ user scoped and are used by the application itself.
"""

from sqlmodel import Field

from .my_model import MyModel


class APIScope(MyModel, table=True):
    """Model for API scopes.

    Attributes:
        module: the module for the API scope.
        subject: the subject for the API scope.
    """

    module: str = Field(max_length=32)
    subject: str = Field(max_length=32)

    @property
    def full_scope_name(self) -> str:
        """Property for the full scope name.

        Returns the complete scope name for this scope.

        Returns:
            The full scope name as string.
        """
        return f'{self.module}.{self.subject}'
