import pytest
from pages.login_page import LoginPage

class TestLogin:

    @pytest.mark.positiveTests
    def test_positive_login(self, driver):
        loginPage = LoginPage(driver)
        loginPage.login("standard_user", "secret_sauce")
        assert "Products" in driver.page_source

    @pytest.mark.negativeTests
    def test_negative_login(self, driver):
        loginPage = LoginPage(driver)
        loginPage.login("standard_user", "ABC123")
        assert "Products" not in driver.page_source