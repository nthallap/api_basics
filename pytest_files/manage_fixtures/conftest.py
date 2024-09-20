import pytest


@pytest.fixture
def sub_fixture(request):
    print("\n*********** Start Execution local ***********")
    print("local conftest fixture")
    print("scope : ", request.scope)
    print("module : ", request.module.__name__)
    print("function : ", request.function.__name__)
    yield 10, 12, 13, 14
    print("\n******* Fixture Teardown local *********")