from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriver, WebElement
from pages.inventory_page import InventoryPage

class LoginPage(BasePage):

    __username_locator = (By.ID, 'user-name') # private member
    __password_locator = (By.ID, 'password') # private member
    __login_button_locator = (By.ID, 'login-button') # private member
    __error_message_locator = (By.XPATH, '//*[@data-test="error"]') # private member

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def _verify_page_loaded_correctly(self):
        assert "Swag Labs" in self._driver.title
        self._wait_until_element_is_visible(self.__login_button_locator)
    
    def login(self, username: str, password: str):
        self._driver.find_element(*self.__username_locator).send_keys(username)
        self._driver.find_element(*self.__password_locator).send_keys(password)
        self._driver.find_element(*self.__login_button_locator).click()
        try:
            return InventoryPage(self._driver)            
        except AssertionError:
            return self
        
    @property
    def error_message(self) -> WebElement: # return value is 'WebElement'
        return self._driver.find_element(*self.__error_message_locator).text
