import pytest
from pages.login_page import LoginPage

class TestLogin:

    @pytest.mark.positiveTests
    def test_positive_login(self, driver):
        loginPage = LoginPage(driver)
        inventoryPage = loginPage.login('standard_user', 'secret_sauce')

    @pytest.mark.negativeTests
    @pytest.mark.parametrize(
        'username,password', 
        [
            ('bad_user', 'secret_sauce'), 
            ('standard_user', 'bad_sauce')])
    def test_negative_login(self, username, password, driver):
        loginPage = LoginPage(driver)
        loginPage.login(username, password)
        assert "Products" not in driver.page_source
        assert loginPage.get_error_message() == 'Epic sadface: Username and password do not match any user in this service'