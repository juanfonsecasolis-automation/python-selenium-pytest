#
# Copyright November 2024 Juan M. Fonseca-Solís.
# Pytest/Selenium minimum working example (MWE).
# Reference: https://www.udemy.com/certificate/UC-36a2f5ef-d733-4d5d-964f-481c55e320e8 (certificate).
#

import pytest
from pages.login_page import LoginPage
from selenium.webdriver.support.wait import WebDriver

class TestLogin:

    @pytest.mark.positiveTests
    @pytest.mark.login
    def test_positive_login(self, driver: WebDriver):
        loginPage = LoginPage(driver)
        inventoryPage = loginPage.login('standard_user', 'secret_sauce')
        assert 0<inventoryPage.get_number_of_inventory_items(), 'There should be at least one inventory item listed.'

    @pytest.mark.negativeTests
    @pytest.mark.login
    @pytest.mark.parametrize(
        'username, password', 
        [
            ('bad_user', 'secret_sauce'), 
            ('standard_user', 'bad_sauce')
        ])
    def test_negative_login(self, username: str, password: str, driver: WebDriver):
        loginPage = LoginPage(driver)
        loginPage.login(username, password)
        assert "Products" not in driver.page_source
        assert loginPage.error_message == 'Epic sadface: Username and password do not match any user in this service'