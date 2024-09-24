import pytest


@pytest.fixture(autouse=True)
def my_fixture():
    return "fixture_value"


def test_example(my_fixture):
    # The fixture is executed automatically
    assert my_fixture == "fixture_value"
