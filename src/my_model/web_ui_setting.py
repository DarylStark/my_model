"""Module that contains the class for a API clients."""

from sqlmodel import Field, Relationship

from .user_scoped_model import UserScopedModel


class WebUISetting(UserScopedModel, table=True):
    """Model for Web UI Settings.

    The Web UI Settings model should be used by Web UIs that use this model to
    set specific settings, like themes and notification settings.

    Attributes:
        setting: the name of the setting
        value: the value for the setting
        user: the user object for the owner.
    """

    setting: str = Field(max_length=32)
    value: str = Field(max_length=32)

    # Relationships
    user: 'User' = Relationship(back_populates='webuisettings')
