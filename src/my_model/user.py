from datetime import datetime
from enum import Enum

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from pydantic import BaseModel, Field
from pyotp import TOTP, random_base32


class UserRole(int, Enum):
    """ Enum containing the roles a user can have. """

    root = 1
    admin = 2
    user = 3


class User(BaseModel):
    """ The user model is meant for local useraccounts """

    created: datetime = Field(default_factory=datetime.utcnow)
    fullname: str = Field(regex=r'^[A-Za-z\- ]+$', max_length=128)
    username: str = Field(regex=r'^Q[a-zA-Z][a-zA-Z0-9_\.]+$', max_length=128)
    email: str = Field(
        regex=r'^[a-z0-9_\-\.]+\@[a-z0-9_\-\.]+\.[a-z\.]+$', max_length=128)
    role: UserRole = Field(default=UserRole.user)
    password_hash: str
    password_date: datetime = Field(default_factory=datetime.utcnow)
    second_factor: None | str = Field(
        default=None,
        regex=r'^[A-Z0-9]+$', max_length=64)

    class Config:
        validate_assignment = True

    def set_password(self, password: str) -> bool:
        """ Sets the password for the user """
        hasher = PasswordHasher()
        self.password_hash = hasher.hash(password)
        self.password_date = datetime.utcnow()

    def set_random_second_factor(self) -> str:
        """ Sets a random second factor secret for the user and
            returns the set secret """
        self.second_factor = random_base32()
        return self.second_factor

    def disable_second_factor(self) -> None:
        """ Disables the second factor for the user """
        self.second_factor = None

    def verify_credentials(self, username: str, password: str, second_factor: str | None = None) -> bool:
        """ Verifies the credentials for a user """

        hasher = PasswordHasher()
        try:
            credentials = (username == self.username and
                           hasher.verify(self.password_hash, password))
        except VerifyMismatchError:
            return False

        if second_factor is None:
            return credentials
        return credentials and second_factor == TOTP(self.second_factor).now()
