#
# Copyright November 2024 Juan M. Fonseca-Solís.
# Pytest/Selenium minimum working example (MWE).
# References: https://www.udemy.com/course/selenium-webdriver-python-course (Dmitry Shyshkin)
#

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryItemComponent(BasePage):

    __instance_index = 1
    __all_instances_locator = (By.CLASS_NAME, 'inventory_item') # private member 
    __add_remove_button_locator = (By.XPATH, f'//*[@class="inventory_item"][{__instance_index}]//button')

    def __init__(self, driver):
        super().__init__(driver)
        
    def _verify_page_loaded_correctly(self):
        self._wait_until_element_is_visible(self.__locator)
        pass

    def add_to_cart(self):
        self._driver.find_element(*self.__add_remove_button_locator).click()
        self._wait_until_element_contains_text(self.__add_remove_button_locator, 'Remove')

    def remove_from_cart(self):
        self._driver.find_element(*self.__add_remove_button_locator).click()
        self._wait_until_element_contains_text(self.__add_remove_button_locator, 'Add to cart')

    @property
    def number_of_instances(self) -> int:
        return len(self._driver.find_elements(*self.__all_instances_locator))

    @property
    def __locator(self):
        return (By.XPATH, f'//*[@class="inventory_item"][{self.__instance_index}]')

    @property
    def instance_index(self) -> int:
        return self.__instance_index
    
    @instance_index.setter
    def instance_index(self, value):
        if 0<value:
            self.__instance_index = value
        else:
            raise Exception('Instance index should be greater than zero.')
        
    def find_instance_index_for_item_name(self, target_item_name: str) -> int:
        all_items = self._driver.find_elements(By.XPATH, '//*[@data-test="inventory-item-name"]')

        for i in range(0, len(all_items)):
            name = all_items[i].text
            if name == target_item_name:
                return i+1
        
        raise Exception(f'Cannot find inventory element with name "{target_item_name}".')