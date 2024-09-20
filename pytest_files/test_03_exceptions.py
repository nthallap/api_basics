import pytest


def test_01():
    with pytest.raises(TypeError):
        2 + "a" == 10

def test_02():
    with pytest.raises(Exception) as e:
        assert 2/0 == 5
    print(e.value, e.type)