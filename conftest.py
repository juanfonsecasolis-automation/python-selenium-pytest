import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser", 
        action="store", 
        default="Chrome", 
        help="Browser to execute the tests.")
    
@pytest.fixture
def params(request):
    params = {}
    params['browser'] = request.config.getoption("--browser")
    return params