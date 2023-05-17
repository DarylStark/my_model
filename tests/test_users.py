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


def test_user_fullname_regex(example_user_no_second_factor: User):
    """ Unit test to check if fullnames that are invalid fail """

    # List with wrong full names
    wrong_full_names = [
        '', 'Daryl1', 'Daryl_Stark', 'Emilia_Clarke'
    ]

    # Loop through them and make sure they fail
    for wrong_username in wrong_full_names:
        with raises(ValueError):
            example_user_no_second_factor.fullname = wrong_username

    # Test correct username
    example_user_no_second_factor.fullname = 'Daryl Stark'
    example_user_no_second_factor.fullname = 'Emilia Clarke'
    example_user_no_second_factor.fullname = 'Emilia-Clarke'


def test_user_username_regex(example_user_no_second_factor: User):
    """ Unit test to check if usernames that are invalid fail """

    # List with wrong usernames
    wrong_usernames = [
        '', 'user name', 'user+name',
        'user@domain.example', '1username', '_username',
        '-username'
    ]

    # Loop through them and make sure they fail
    for wrong_username in wrong_usernames:
        with raises(ValueError):
            example_user_no_second_factor.username = wrong_username

    # Test correct username
    example_user_no_second_factor.username = 'daryl.stark'
    example_user_no_second_factor.username = 'emilia.clarke'
    example_user_no_second_factor.username = 'emilia_clarke'


def test_user_email_regex(example_user_no_second_factor: User):
    """ Unit test to check if emailaddresses that are invalid fail """

    # List with wrong emailaddress
    wrong_mail = [
        '', 'fake_mail', 'daryl@daryl'
    ]

    # Loop through them and make sure they fail
    for wrong_address in wrong_mail:
        with raises(ValueError):
            example_user_no_second_factor.email = wrong_address

    # Test correct username
    example_user_no_second_factor.email = 'daryl.stark@dstark.nl'
    example_user_no_second_factor.email = 'emilia.clarke@dstark.nl'
    example_user_no_second_factor.email = 'emilia_clarke@dstark.co.uk'


def test_user_second_factor_regex(example_user_no_second_factor: User):
    """ Unit test to check if second factors that are invalid fail
    """

    # List with wrong second factors
    wrong_second_factors = [
        'ape', 'daryl', '123ape'
    ]

    # Loop through them and make sure they fail
    for wrong_second_factors in wrong_second_factors:
        with raises(ValueError):
            example_user_no_second_factor.second_factor = wrong_second_factors

    # Test correct username
    example_user_no_second_factor.second_factor = 'ABCDEFG'
    example_user_no_second_factor.second_factor = '123ABCEF'
    example_user_no_second_factor.second_factor = 'HIJKLMN'


def test_user_correct_credentials(example_user_no_second_factor: User):
    """ Test if credentials can be set and verified """

    # Test username/password combination
    assert example_user_no_second_factor.verify_credentials(
        username='fake.user',
        password='testtest'), "Credential verification failed (without second factor)"

    # Create a OTP for the user
    otp_secret = example_user_no_second_factor.set_random_second_factor()

    # Test username/password/second factor combination
    assert example_user_no_second_factor.verify_credentials(
        username='fake.user',
        password='testtest',
        second_factor=TOTP(otp_secret).now()), "Credential verification failed (with second factor)"


def test_user_incorrect_credentials(example_user_no_second_factor: User):
    """ Test if wrong credentials result in error """

    # Test username/password combination
    assert not example_user_no_second_factor.verify_credentials(
        username='fake.user',
        password='somethingelse'), "Credential didn't fail when they should've (without second factor)"

    # Create a OTP for the user
    _ = example_user_no_second_factor.set_random_second_factor()

    # Test username/password/second factor combination
    assert not example_user_no_second_factor.verify_credentials(
        username='fake.user',
        password='testtest',
        second_factor='alsowrong'), "Credential didn't fail when they should've (with second factor)"
