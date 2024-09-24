import pytest


def test_01():
    with pytest.raises(TypeError):
        x = 2 + "a"


def test_02():
    with pytest.raises(Exception) as e:
        assert 2 / 0 == 5
    print(e.value, e.type)
