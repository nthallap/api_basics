import pytest
import os
from datetime import datetime


@pytest.fixture
def suite_fixture():
    print("\n*********** Start Execution Main ***********")
    print("Main level conftest fixture")
    yield [1, 2, 3, 4, 5, 6, 7]
    print("\n******* Fixture Teardown Main *********")


def pytest_addoption(parser):
    parser.addoption("--cmdopt", default="QA")


# reading command line arguments option 1
@pytest.fixture()
def cmd_opt_read(request):
    cmd_option = request.config.getoption("--cmdopt")
    return cmd_option


# reading command line arguments option 2
@pytest.fixture()
def cmd_opt_read02(pytestconfig):
    cmd_option = pytestconfig.getoption("--cmdopt")
    return cmd_option


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    root_path = os.path.dirname(__file__).replace("tests", "reports")
    dir_name = datetime.now().strftime("%m_%d_%Y_%H%M%S")
    dir_path = os.path.join(root_path, dir_name)
    file_path = os.path.join(dir_path, 'report.html')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    config.option.htmlpath = file_path
    config.option.log_format = '%(asctime)s  %(levelname)s  %(message)s'
    print(config, "***************************************", config.option)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_setup(item):
    config = item.config
    logging_plugin = config.pluginmanager.get_plugin("logging-plugin")
    file_path = config.option.htmlpath.replace('report.html',
                                               item._request.node.name + ".log")
    logging_plugin.set_log_path(file_path)
    yield
