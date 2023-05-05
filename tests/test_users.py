from datetime import datetime

from pyotp import TOTP
from pytest import fixture, raises

from my_model.user import User


@fixture
def example_user_no_second_factor() -> User:
    user = User(
        created=datetime.utcnow(),
        fullname='Fake fullname',
        username='fake.user',
        email='fakse@fake.example',
        password_hash='xxxxx',
        password_date=datetime.utcnow(),
        second_factor=None)
    user.set_password('testtest')
    return user


def test_users_correct_credentials(example_user_no_second_factor: User):
    """ Test if credentials can be set and verified """

    # Test username/password combination
    assert example_user_no_second_factor.verify_credentials(
        username='fake.user',
        password='testtest')

    # Create a OTP for the user
    otp_secret = example_user_no_second_factor.set_random_second_factor()

    # Test username/password/second factor combination
    assert example_user_no_second_factor.verify_credentials(
        username='fake.user',
        password='testtest',
        second_factor=TOTP(otp_secret).now())


def test_users_incorrect_credentials(example_user_no_second_factor: User):
    """ Test if wrong credentials result in error """

    # Test username/password combination
    assert not example_user_no_second_factor.verify_credentials(
        username='fake.user',
        password='somethingelse')

    # Create a OTP for the user
    _ = example_user_no_second_factor.set_random_second_factor()

    # Test username/password/second factor combination
    assert not example_user_no_second_factor.verify_credentials(
        username='fake.user',
        password='testtest',
        second_factor='alsowrong')
