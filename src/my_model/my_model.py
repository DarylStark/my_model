"""Module that contains the base class for all models."""

import random
import string

from pydantic import validate_call
from sqlmodel import Field, SQLModel
from sqlmodel._compat import SQLModelConfig


class MyModel(SQLModel):
    """SQLmodel basemodel for all models.

    Should be used for all models. This base class defines the Pydantic
    configuration that all models should use. Because we use SQLmodel, these
    models are usable for generic modeling _and_ for SQLalchemy ORM.

    Attributes:
        id: the unique ID for this object. If this object is used for a SQL
            database, it is the primary key.
    """

    id: int | None = Field(default=None, primary_key=True)
    model_config = SQLModelConfig(validate_assignment=True)
    
    # The `__pydantic_extra__` attribute is set to None, just to make sure the
    # library can find this attribute. It may be unneeded in future versions of
    # SQLmodel, but right now, in version `0.0.14`, is is needed or it will
    # trigger a error.
    __pydantic_extra__ = None

    @validate_call
    def get_random_string(self,
                          min_length: int,
                          max_length: int,
                          include_punctation: bool = True) -> str:
        """
        Return a random generated string.

        Can be used to generate a random string for tokens, passwords or other
        secrets. The min_length and max_length arguments can be used to set the
        size limits for the random string. The method will create a string of
        random length within these limits. If you need a specific length, make
        sure that both min_length and max_length are of equal val23
        ue.

        Args:
            min_length: the minimum length of the generated random string
            max_length: the maximum length of the generated random string
            include_punctation: defines if punctation should be used

        Returns:
            A string with the randomly generated characters.
        """
        # Create the characterset
        characters = string.ascii_letters
        characters += string.digits

        if include_punctation:
            characters += string.punctuation

        # Create the random character string
        length = random.randint(min_length, max_length)
        random_token_chars = [random.choice(characters)
                              for i in range(0, length)]
        random_string = ''.join(random_token_chars)

        # Return the created string
        return random_string
