from pages.with_upper_menu_page import WithUpperMenuPage
from selenium.webdriver.support.wait import WebDriver
from selenium.webdriver.common.by import By

class InventoryPage(WithUpperMenuPage):

    __inventory_item_name_locator = (By.XPATH, '//*[@data-test="inventory-item-name"]')  # private member
    __inventory_item_container = (By.CLASS_NAME, 'inventory_item') # private member

    def __init__(self, driver: WebDriver):
        super(InventoryPage, self).__init__(driver)

    def _verify_page_loaded_correctly(self):
        assert "/inventory.html" in self._driver.current_url
        self._wait_until_element_is_visible(self.__inventory_item_name_locator)

    def get_number_of_inventory_items(self) -> int:
        # return type is 'int'
        return len(self._driver.find_elements(*self.__inventory_item_container))
    