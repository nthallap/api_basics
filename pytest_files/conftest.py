import pytest


@pytest.fixture
def suite_fixture():
    print("\n*********** Start Execution Main ***********")
    print("Main level conftest fixture")
    yield [1, 2, 3, 4, 5, 6, 7]
    print("\n******* Fixture Teardown Main *********")


def pytest_addoption(parser):
    parser.addoption("--cmdopt", default="QA")

@pytest.fixture()
def cmd_opt_read(request):
    cmd_option = request.config.getoption("--cmdopt")
    return cmd_option

@pytest.fixture()
def cmd_opt_read02(pytestconfig):
    cmd_option = pytestconfig.getoption("--cmdopt")
    return cmd_option