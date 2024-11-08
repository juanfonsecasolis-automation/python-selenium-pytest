import pytest
from selenium.webdriver.common.by import By

class TestPython:

    @pytest.mark.python
    def test_packing_argument(self):
        var = By.XPATH, '//*'
        assert type(var).__name__=='tuple'