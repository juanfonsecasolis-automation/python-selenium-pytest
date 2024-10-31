import pytest
from helpers.driver_manager import get_driver
from pages.login_page import LoginPage

class TestLogin:

    @pytest.fixture()
    def driver(self, params):
        self.driver = get_driver(params['browser'])
        self.driver.get("https://www.saucedemo.com/")
        yield
        self.driver.close()

    @pytest.mark.positiveTests
    def test_positive_login(self, driver):
        loginPage = LoginPage(driver)
        loginPage.login("standard_user", "secret_sauce")
        assert "Products" in self.driver.page_source

    @pytest.mark.negativeTests
    def test_negative_login(self, driver):
        loginPage = LoginPage(driver)
        loginPage.login("standard_user", "ABC123")
        assert "Products" not in self.driver.page_source