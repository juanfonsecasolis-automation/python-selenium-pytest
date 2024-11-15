import pytest
from selenium.webdriver.support.wait import WebDriver
from pages.login_page import LoginPage, InventoryPage

class TestInventory:

    @pytest.mark.positiveTests
    @pytest.mark.inventory
    def test_add_items_to_cart(self, driver: WebDriver):
        loginPage = LoginPage(driver)
        inventory_page = loginPage.login('standard_user', 'secret_sauce')
        expected_value = inventory_page.get_number_items_on_the_cart()+1
        inventory_page.add_one_item_to_the_cart()
        assert inventory_page.get_number_items_on_the_cart() == expected_value