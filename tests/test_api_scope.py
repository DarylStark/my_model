from pytest import fixture, raises

from my_model.global_models import APIScope


@fixture
def example_api_scope() -> APIScope:
    token = APIScope(module='mymodule', subject='mysubject')
    return token


def test_api_scope_full_scope_name(example_api_scope: APIScope) -> None:
    """ Unit test to see if the full name is correct """

    assert example_api_scope.full_scope_name == 'mymodule.mysubject'
