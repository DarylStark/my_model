from pytest import fixture, raises

from my_model.user_scoped_models import APIToken


@fixture
def example_api_token() -> APIToken:
    token = APIToken(title='testtoken')
    return token


def test_api_token_token_regex(example_api_token: APIToken) -> None:
    """ Unit test to test the regex for tokens """

    # Invalid tokens
    with raises(ValueError):
        example_api_token.token = 'abcdefghijklmnopqrstuvwxyz'
        example_api_token.token = 'xyz'
        example_api_token.token = 'qwertyuiopASDFGHJKLzxcvbnm--909'

    # Valid tokens
    example_api_token.token = 'qwertyuiopASDFGHJKLzxcvbnm009909'


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
