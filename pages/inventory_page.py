#
# Copyright November 2024 Juan M. Fonseca-Solís.
# Pytest/Selenium minimum working example (MWE).
# Reference: https://www.udemy.com/certificate/UC-36a2f5ef-d733-4d5d-964f-481c55e320e8 (certificate).
#

from pages.with_upper_menu_page import WithUpperMenuPage
from selenium.webdriver.support.wait import WebDriver
from pages.components.inventory_item_page import InventoryItemComponent

class InventoryPage(WithUpperMenuPage):

    _inventory_item_component = None

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._inventory_item_component = InventoryItemComponent(driver)

    def _verify_page_loaded_correctly(self):
        assert "/inventory.html" in self._driver.current_url
    
    def add_item_to_the_cart(self, item_name: str):
        self._inventory_item_component.instance_index = self._inventory_item_component.find_instance_index_for_item_name(item_name)
        self._inventory_item_component.add_to_cart()

    def remove_item_from_the_cart(self, item_name: str):
        self._inventory_item_component.instance_index = self._inventory_item_component.find_instance_index_for_item_name(item_name)
        self._inventory_item_component.remove_from_cart()

    def get_number_of_inventory_items(self) -> int:
        return self._inventory_item_component.number_of_instances
    