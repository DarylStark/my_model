"""Module that contains the base class for all models."""

import random
import string
from typing import Any

from pydantic import BaseModel, validate_arguments


class Model(BaseModel):
    """Pydantic basemodel for all models.

    Should be used for all models. This base class defines the Pydantic
    configuration that all models should use.

    Attributes:
        id: the unique ID for this object
    """

    id: int | None = None

    # Hidden fields
    _hidden_fields: dict[str, Any] = {}

    def set_hidden(self, name: str, value: Any) -> None:
        """Set a hidden value.

        Sets a hidden value in the object. These values can be used for
        connection to a database, for example.

        Args:
            name: the name of the hidden data.
            value: the value.
        """
        self._hidden_fields[name] = value

    def get_hidden(self, name: str, default: Any = None) -> Any:
        """Get a hidden value.

        Returns a hidden value.

        Args:
            name: the name of the hidden data.
            default: the default value in case the hidden data is not found.

        Returns:
            Any: the value of the hidden data.
        """
        return self._hidden_fields.get(name, default)

    class Config:
        """Config for the models.

        Attributes:
            validate_assignment: specifies if assigned values should be
                validated by Pydantic. If this is set to False, only
                assignments in the constructor are validated.
        """

        validate_assignment = True

    @validate_arguments
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
        sure that both min_length and max_length are of equal value.

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
