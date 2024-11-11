import pytest
from helpers.driver_manager import get_driver
from pages.base_page import BasePage

def pytest_addoption(parser):
    parser.addoption(
        "--browser", 
        action="store", 
        default="Chrome", 
        help="Browser to execute the tests.")

@pytest.fixture()
def driver(params):
    driver = get_driver(params['browser'])
    driver.get(BasePage.base_url)
    yield driver
    driver.close()    

@pytest.fixture
def params(request):
    params = {}
    params['browser'] = request.config.getoption("--browser")
    return params