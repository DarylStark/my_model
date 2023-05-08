from pytest import fixture, raises
from my_model.usersession import UserSession


@fixture
def example_user_session() -> UserSession:
    usersession = UserSession(title='User session')
    return usersession


def test_random_secret_length(example_user_session: UserSession):
    """ Unit test to check if the generated secret length is
        correct """

    # Generate a random secret of a specific length
    size = (32, 64)
    example_user_session.set_random_secret(
        min_length=size[0],
        max_length=size[1])

    if example_user_session.secret:
        # Check if the length is correct
        assert len(example_user_session.secret) >= size[0] and len(
            example_user_session.secret) <= size[1], "Secret length is not correct"
        return

    # Random secret was nog generated
    assert False, "Secret was not set"
