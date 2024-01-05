"""Tests fir Tags."""
# pylint: disable=redefined-outer-name
from pytest import fixture, raises
import pytest

from my_model.user_scoped_models import Tag


@fixture
def example_tag() -> Tag:
    """Fixture that creates a Tag object.

    Returns:
        The created Tag object.
    """
    tag = Tag(title='testtoken')
    return tag


@pytest.mark.parametrize('invalid_color', [
    'red',
    'green',
    'blue',
    'fff',
    '9090hj'
])
def test_tag_invalid_color_regex(
        example_tag: Tag,
        invalid_color: str) -> None:
    """Unit test to test invalid color.

    Args:
        example_tag: a tag object for the test.
        invalid_color: the color to test.
    """

    # Invalid colors
    with raises(ValueError):
        example_tag.color = invalid_color


@pytest.mark.parametrize('valid_color', [
    '00ff00',
    '1590fc',
    '1590FC',
    'FFFFFF'
])
def test_tag_valid_color_regex(
        example_tag: Tag,
        valid_color: str) -> None:
    """Unit test to test valid colors.

    Args:
        example_tag: a tag object for the test.
        valid_color: the color to test.
    """
    example_tag.color = valid_color
