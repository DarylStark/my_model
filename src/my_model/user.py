"""Module that contains the class for a User."""

from datetime import datetime
from enum import Enum

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from pydantic import validate_arguments
from pyotp import TOTP, random_base32
from sqlmodel import Field

from ._model import Model


class UserRole(int, Enum):
    """The roles a user can have.

    Attributes:
        ROOT: for root users; users with god-mode permissions.
        ADMIN: for admin users; users with the permissions to create other
            'normal' users.
        USER: normal users
    """

    ROOT = 1
    USER = 2


class User(Model):
    """Model for Users.

    The user model is meant for local useraccounts.

    Attributes:
        created: the datetime when this user was created
        fullname: the fullname for the user
        username: the username for the user
        email: the emailaddress of the user
        role: the role of the user (see UserRole)
        password_hash: the hashed password of the user
        password_date: the date when the password was set
        second_factor: either a random base32 that indicates a secret for the
            second factor of the user, or None if no secret is set.
    """

    created: datetime = Field(default_factory=datetime.utcnow)
    fullname: str = Field(regex=r'^[A-Za-z\- ]+$', max_length=128)
    username: str = Field(regex=r'^[a-zA-Z][a-zA-Z0-9_\.]+$', max_length=128)
    email: str = Field(
        regex=r'^[a-z0-9_\-\.]+\@[a-z0-9_\-\.]+\.[a-z\.]+$', max_length=128)
    role: UserRole = Field(default=UserRole.USER)
    password_hash: str | None = None
    password_date: datetime = Field(default_factory=datetime.utcnow)
    second_factor: None | str = Field(
        default=None,
        regex=r'^[A-Z0-9]+$', max_length=64)

    @validate_arguments
    def set_password(self, password: str) -> None:
        """Set the password for the user.

        Args:
            password: the password for the user.
        """
        hasher = PasswordHasher()
        self.password_hash = hasher.hash(password)
        self.password_date = datetime.utcnow()

    @validate_arguments
    def set_random_second_factor(self) -> str:
        """Set a random second factor secret for the user.

        Returns:
            The generated second factor secret.
        """
        self.second_factor = random_base32()
        return self.second_factor

    @validate_arguments
    def disable_second_factor(self) -> None:
        """Disable the second factor for the user."""
        self.second_factor = None

    @validate_arguments
    def verify_credentials(self,
                           username: str,
                           password: str,
                           second_factor: str | None = None) -> bool:
        """Verify the credentials for a user.

        Args:
            username: the username to verify
            password: the password to verify
            second_factor: the second factor for the user, or None if this
                doesn't need to be validated.

        Returns:
            True if the credentials where corret for this useraccount. False if
            these credentials where not correct.
        """
        hasher = PasswordHasher()
        try:
            if self.password_hash:
                credentials = (username == self.username and
                               hasher.verify(self.password_hash, password))
            else:
                raise VerifyMismatchError
        except VerifyMismatchError:
            return False

        if self.second_factor:
            return (credentials and
                    second_factor == TOTP(self.second_factor).now())

        return credentials
