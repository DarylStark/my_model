from pydantic import BaseModel, Field


class Tag(BaseModel):
    """ The tag model is meant to represent a tag. A tag can be
        given to a multitude of resources in the application, like
        days, notes, RSS feeds, etc. They are meant to group
        everything together that needs to be together """

    title: str = Field(max_length=128)
    color: str | None = Field(
        default=None, regex=r'^[a-fA-F0-9]{6}$', min_length=6, max_length=6)
