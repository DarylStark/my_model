from pytest import fixture, raises

from my_model.tag import Tag


@fixture
def example_tag() -> Tag:
    tag = Tag(title='testtoken')
    return tag


def test_tag_color_regex(example_tag: Tag) -> None:
    """ Unit test to test the regex for the color """

    assert False

    # Invalid colors
    with raises(ValueError):
        example_tag.color = 'red'
        example_tag.color = 'green'
        example_tag.color = 'blue'
        example_tag.color = 'fff'
        example_tag.color = '9090hj'

    # Valid colors
    example_tag.color = '00ff00'
    example_tag.color = '1590fc'
    example_tag.color = '1590FC'
    example_tag.color = 'FFFFFF'
