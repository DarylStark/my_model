"""Module that contains the base class for models that are user scoped."""

from sqlmodel import Field

from .my_model import MyModel


class UserScopedModel(MyModel):
    """Basemodel for models that are user scoped.

    Defines the `user_id` attribute for models that are scoped to a specific
    user. By putting this in a seperate base class, we can prevent duplicate
    code.

    Attributes:
        user_id: the unique ID for a user.
    """

    user_id: int | None = Field(foreign_key='user.id')
