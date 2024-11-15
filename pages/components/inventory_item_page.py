from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriver
from selenium.webdriver.common.by import By

class InventoryItemComponent(BasePage):

    __instance_index = 1
    __all_instances_locator = (By.CLASS_NAME, 'inventory_item') # private member 

    def __init__(self, driver):
        super().__init__(driver)
        
    def _verify_page_loaded_correctly(self):
        #self._wait_until_element_is_visible(self.__locator)
        pass

    def get_number_of_instances(self) -> int:
        return len(self._driver.find_elements(*self.__all_instances_locator))
    
    def add_to_cart(self):
        add_button_locator = (By.XPATH, f'//*[@class="inventory_item"][{self.__instance_index}]//button')   # need to refactor getting the locator from __locator
        self._driver.find_element(*add_button_locator).click()
        self._wait_until_element_contains_text(add_button_locator, 'Remove')

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