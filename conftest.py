#
# Copyright November 2024 Juan M. Fonseca-Solís
# Pytest/Selenium minimum working example (MWE)
#

import pytest
from helpers.driver_manager import get_driver
from pages.base_page import BasePage

def pytest_addoption(parser):

    parser.addoption(
        "--browser", 
        action="store", 
        default="Chrome", 
        help="Browser to execute the tests.")  
    
    parser.addoption(
        "--headless", 
        action="store", 
        default="False", 
        help="Execute tests in headless mode.")  

@pytest.fixture
def params(request):
    params = {}
    params['browser'] = request.config.getoption("--browser")
    params['headless'] = request.config.getoption("--headless")
    return params

@pytest.fixture()
def driver(params):
    # test set up
    driver = get_driver(params)
    driver.get(BasePage.base_url)
    yield driver
    # teardown
    driver.close()