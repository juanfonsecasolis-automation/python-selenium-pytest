from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait, WebDriver, WebElement
from selenium.webdriver.support import expected_conditions as EC
from pages.inventory_page import InventoryPage

class LoginPage(BasePage):

    __username_locator = (By.ID, 'user-name') # private attribute
    __password_locator = (By.ID, 'password') # private attribute
    __login_button_locator = (By.ID, 'login-button') # private attribute
    __error_message_locator = (By.XPATH, '//*[@data-test="error"]') # private attribute

    def __init__(self, driver: WebDriver):
        super(LoginPage, self).__init__(driver)

    def _verify_page_loaded_correctly(self):
        assert "Swag Labs" in self._driver.title
        self._wait_until_element_is_visible(self.__login_button_locator)
    
    def login(self, username: str, password: str):
        self._driver.find_element(*self.__username_locator).send_keys(username)
        self._driver.find_element(*self.__password_locator).send_keys(password)
        self._driver.find_element(*self.__login_button_locator).click()
        try:
            return InventoryPage(self._driver)
        except:
            return self
        
    @property
    def error_message(self) -> WebElement: 
        # return value is 'WebElement'
        return self._driver.find_element(*self.__error_message_locator).text
