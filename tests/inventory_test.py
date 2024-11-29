#
# Copyright November 2024 Juan M. Fonseca-Solís.
# Pytest/Selenium minimum working example (MWE).
# Reference: https://www.udemy.com/certificate/UC-36a2f5ef-d733-4d5d-964f-481c55e320e8 (certificate).
#

import pytest
from selenium.webdriver.support.wait import WebDriver
from pages.login_page import LoginPage, InventoryPage

class TestInventory:

    @pytest.fixture
    def inventory_page(self, driver: WebDriver):
        # set-up
        loginPage = LoginPage(driver)
        inventory_page = loginPage.login('standard_user', 'secret_sauce')
        return inventory_page

    @pytest.mark.positiveTests
    @pytest.mark.inventory
    def test_adding_items_to_the_cart_increases_number_on_cart_badge(
            self, 
            inventory_page: InventoryPage
        ):        
        expected_value = inventory_page.number_of_items_on_the_cart+1
        inventory_page.add_item_to_the_cart('Sauce Labs Backpack')
        assert inventory_page.number_of_items_on_the_cart == expected_value

    @pytest.mark.positiveTests
    @pytest.mark.inventory
    def test_removing_items_from_the_cart_decreases_number_on_cart_badge(
            self, 
            inventory_page: InventoryPage
        ):        
        inventory_page.add_item_to_the_cart('Sauce Labs Backpack')
        expected_value = inventory_page.number_of_items_on_the_cart-1
        inventory_page.remove_item_from_the_cart('Sauce Labs Backpack')
        assert inventory_page.number_of_items_on_the_cart == expected_value