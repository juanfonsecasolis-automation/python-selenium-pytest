#
# Copyright November 2024 Juan M. Fonseca-Solís.
# Pytest/Selenium minimum working example (MWE).
# Reference: https://www.udemy.com/certificate/UC-36a2f5ef-d733-4d5d-964f-481c55e320e8 (certificate).
#

from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriver
from selenium.webdriver.common.by import By

class WithUpperMenuPage(BasePage):

    __hamburguer_menu_locator = (By.ID, 'react-burger-menu-btn')    # private member
    __cart_icon_locator = (By.XPATH, "//*[@data-test='shopping-cart-link']") # private member
    __shopping_cart_badge = (By.XPATH, "//*[@data-test='shopping-cart-badge']") # private member

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def _verify_page_loaded_correctly(self):
        assert self._driver.find_element(self.__hamburguer_menu_locator).is_displayed
        assert self._driver.find_element(self.__cart_icon_locator).is_displayed

    @property
    def number_of_items_on_the_cart(self) -> int:
        if len(self._driver.find_elements(*self.__shopping_cart_badge)) == 0:
            return 0
        else:
            return int(self._driver.find_element(*self.__shopping_cart_badge).text)