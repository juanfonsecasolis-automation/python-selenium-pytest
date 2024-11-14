from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriver
from selenium.webdriver.common.by import By

class WithUpperMenuPage(BasePage):

    __hamburguer_menu_locator = (By.ID, 'react-burger-menu-btn')    # private attribute
    __cart_icon_locator = (By.XPATH, "//*[@data-test='shopping-cart-link']") # private attribute

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def _verify_page_loaded_correctly(self):
        assert self._driver.find_element(self.__hamburguer_menu_locator).is_displayed
        assert self._driver.find_element(self.__cart_icon_locator).is_displayed