from my_model.my_model import MyModel
import pytest


@pytest.mark.parametrize('min, max',
                         [
                             (1, 10), (2, 20), (25, 30), (50, 100)
                         ]
                         )
def test_base_model_get_random_token(min: int, max: int) -> None:
    """Unit test to test the `get_random_token` method."""
    model = MyModel()
    random_string = model.get_random_string(min_length=min, max_length=max,
                                            include_punctation=True)
    assert len(random_string) >= min
    assert len(random_string) <= max
