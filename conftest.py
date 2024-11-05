import pytest
from helpers.driver_manager import get_driver

def pytest_addoption(parser):
    parser.addoption(
        "--browser", 
        action="store", 
        default="Chrome", 
        help="Browser to execute the tests.")

@pytest.fixture()
def driver(params):
    driver = get_driver(params['browser'])
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.close()    

@pytest.fixture
def params(request):
    params = {}
    params['browser'] = request.config.getoption("--browser")
    return params