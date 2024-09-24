import pytest


@pytest.fixture(autouse=True)
def myfixture():
    print("\nI am a fixture setup")
    print("I am a suite setup")
    yield [1, 2, 3, 4, 5]
    print("\nI am a Tear down")  # after yield part will execute after test case execution completed
    print("I am a suite tear down")  # This is a kind of teardown


@pytest.fixture(params=[(1, 3), [2, 3]], ids=["tuple", 'list'])
def param_fixture(request):
    return request.param


def test_param_fixture(param_fixture):
    assert type(param_fixture) in [list, tuple]
    print(myfixture, "************")


def test_fixture01(myfixture):
    print("i am a running after fixture")
    print(myfixture)


@pytest.mark.xfail(reason="by using this way of fixuters we can not use return values")
@pytest.mark.usefixtures("myfixture")
def test_fixture02():
    print("This is a calling fixture in differ way")
    print(myfixture[1])  # this will raises an error
