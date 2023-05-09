from datetime import datetime

from pyotp import TOTP
from pytest import fixture, raises

from my_model.api_token import APIToken


@fixture
def example_api_token() -> APIToken:
    token = APIToken(title='testtoken')
    return token


def test_api_token_random_token(example_api_token: APIToken) -> None:
    """ Unit test to see if we can set a random token """

    # Set a random token for the API Token
    token = example_api_token.set_random_token()
    assert token == example_api_token.token


def test_api_token_overwrite(example_api_token: APIToken) -> None:
    """ Test if we can overwrite the token with Force """

    token = example_api_token.set_random_token()
    new_token = example_api_token.set_random_token(force=True)
    assert token != new_token


def test_api_token_not_overwrite(example_api_token: APIToken) -> None:
    """ Test if we get an error when we try to overwrite the token
        after it is already set """

    token = example_api_token.set_random_token()
    with raises(PermissionError):
        _ = example_api_token.set_random_token()
