from pytest import fixture, raises

from my_model.user_scoped_models import APIClient


@fixture
def example_api_client() -> APIClient:
    client = APIClient(app_name='testapp', app_publisher='Daryl Stark')
    return client


def test_api_client_token_regex(example_api_client: APIClient) -> None:
    """ Unit test to test the regex for tokens """

    # Invalid tokens
    with raises(ValueError):
        example_api_client.token = 'abcdefghijklmnopqrstuvwxyz'
        example_api_client.token = 'xyz'
        example_api_client.token = 'qwertyuiopASDFGHJKLzxcvbnm--909'

    # Valid tokens
    example_api_client.token = 'qwertyuiopASDFGHJKLzxcvbnm009909'


def test_api_client_url_regex(example_api_client: APIClient) -> None:
    """ Unit test to test the regex for tokens """

    # Invalid URLs
    with raises(ValueError):
        example_api_client.redirect_url = 'http:/example.com/api?redirect=1'
        example_api_client.redirect_url = 'https:/example.com/api?redirect=1'

    # Valid URLs
    example_api_client.redirect_url = 'http://example.com/api?redirect=1'
    example_api_client.redirect_url = 'https://example.com/api?redirect=1'


def test_api_client_random_token(example_api_client: APIClient) -> None:
    """ Unit test to see if we can set a random token """

    # Set a random token for the API token
    token = example_api_client.set_random_token()
    assert token == example_api_client.token


def test_api_client_overwrite(example_api_client: APIClient) -> None:
    """ Test if we can overwrite the token with Force """

    token = example_api_client.set_random_token()
    new_token = example_api_client.set_random_token(force=True)
    assert token != new_token


def test_api_client_not_overwrite(example_api_client: APIClient) -> None:
    """ Test if we get an error when we try to overwrite the token
        after it is already set """

    token = example_api_client.set_random_token()
    with raises(PermissionError):
        _ = example_api_client.set_random_token()
