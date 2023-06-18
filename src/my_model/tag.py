"""Module that contains the class for a API clients."""

from sqlmodel import Field, Relationship

from .user import User
from .user_scoped_model import UserScopedModel


class Tag(UserScopedModel):
    """Model for Tags.

    The tag model is meant to represent a tag. A tag can be given to a
    multitude of resources in the application, like days, notes, RSS feeds,
    etc. They are meant to group everything together that needs to be together.

    Attributes:
        title: the name of the tag
        color: a specific color for the tag. This color can be used by
            view-services to display the tag in a distinguishable way. The
            color should be represented as a 6-character hex string (RGB).
    """

    title: str = Field(max_length=128)
    color: str | None = Field(
        default=None, regex=r'^[a-fA-F0-9]{6}$', min_length=6, max_length=6)
    user: User = Relationship(back_populates='tags')
