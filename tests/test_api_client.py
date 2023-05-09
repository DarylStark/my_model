from datetime import datetime

from pyotp import TOTP
from pytest import fixture, raises

from my_model.api_client import APIClient


@fixture
def example_api_client() -> APIClient:
    client = APIClient(app_name='testapp', app_publisher='Daryl Stark')
    return client


def test_api_token_random_token(example_api_client: APIClient) -> None:
    """ Unit test to see if we can set a random token """

    # Set a random token for the API token
    token = example_api_client.set_random_token()
    assert token == example_api_client.token


def test_api_token_overwrite(example_api_client: APIClient) -> None:
    """ Test if we can overwrite the token with Force """

    token = example_api_client.set_random_token()
    new_token = example_api_client.set_random_token(force=True)
    assert token != new_token


def test_api_token_not_overwrite(example_api_client: APIClient) -> None:
    """ Test if we get an error when we try to overwrite the token
        after it is already set """

    token = example_api_client.set_random_token()
    with raises(PermissionError):
        _ = example_api_client.set_random_token()
