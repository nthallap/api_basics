import pytest


@pytest.fixture(params=[(1,2), [2,3]], ids=[tuple, list])
def param_fixture(request):
    return request.param

@pytest.fixture(params=["access", "print"])
def param_fixture02(request):
    return request.param


def test_param_fixture(param_fixture):
    assert type(param_fixture) in [list, tuple]
    print(param_fixture)

def test_param_fixture2(param_fixture, param_fixture02):
    if param_fixture02 == "access":
        print(param_fixture[0])
    elif param_fixture02 == "print":
        print(param_fixture)