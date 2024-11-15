from pages.with_upper_menu_page import WithUpperMenuPage
from selenium.webdriver.support.wait import WebDriver
from selenium.webdriver.common.by import By
from pages.components.inventory_item_page import InventoryItemComponent

class InventoryPage(WithUpperMenuPage):

    _inventory_item_component = None

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._inventory_item_component = InventoryItemComponent(driver)

    def _verify_page_loaded_correctly(self):
        assert "/inventory.html" in self._driver.current_url
    
    def add_one_item_to_the_cart(self):
        self._inventory_item_component.instance_index = 1
        self._inventory_item_component.add_to_cart()
    