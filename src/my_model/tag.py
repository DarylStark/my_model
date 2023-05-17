"""Module that contains the class for a API clients."""

from pydantic import Field
from ._model import Model


class Tag(Model):
    """Model for Tags.

    The tag model is meant to represent a tag. A tag can be given to a
    multitude of resources in the application, like days, notes, RSS feeds,
    etc. They are meant to group everything together that needs to be together.

    Class attributes:
        title: the name of the tag
        color: a specific color for the tag. This color can be used by
            view-services to display the tag in a distinguishable way. The
            color should be represented as a 6-character hex string (RGB).
    """

    title: str = Field(max_length=128)
    color: str | None = Field(
        default=None, regex=r'^[a-fA-F0-9]{6}$', min_length=6, max_length=6)
