from time import sleep
import pytest
from selenium.webdriver.support.wait import WebDriver
from pages.login_page import LoginPage, InventoryPage

class TestInventory:

    @pytest.fixture
    def inventory_page(self, driver: WebDriver):
        loginPage = LoginPage(driver)
        inventory_page = loginPage.login('standard_user', 'secret_sauce')
        return inventory_page

    @pytest.mark.positiveTests
    @pytest.mark.inventory
    def test_adding_items_to_the_cart_increases_number_on_cart_badge(self, driver: WebDriver, inventory_page: InventoryPage):        
        expected_value = inventory_page.number_of_items_on_the_cart+1
        inventory_page.add_one_item_to_the_cart()
        assert inventory_page.number_of_items_on_the_cart == expected_value

    @pytest.mark.positiveTests
    @pytest.mark.inventory
    def test_removing_items_from_the_cart_decreases_number_on_cart_badge(self, driver: WebDriver, inventory_page: InventoryPage):        
        inventory_page.add_one_item_to_the_cart()
        expected_value = inventory_page.number_of_items_on_the_cart-1
        inventory_page.remove_one_item_from_the_cart()
        assert inventory_page.number_of_items_on_the_cart == expected_value