from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.inventory_page import InventoryPage

class LoginPage(BasePage):

    __username_locator = By.ID, 'user-name'
    __password_locator = By.ID, 'password'
    __login_button_locator = By.ID, 'login-button'
    __error_message_locator = By.XPATH, '//*[@data-test="error"]'

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def _verify_page_loaded_correctly(self):
        assert "Swag Labs" in self._BasePage__driver.title
        WebDriverWait(self._BasePage__driver, self._BasePage__explicit_wait_timeout_seconds).until(EC.presence_of_element_located(self.__login_button_locator))
    
    def login(self, username, password):
        self._BasePage__driver.find_element(*self.__username_locator).send_keys(username)
        self._BasePage__driver.find_element(*self.__password_locator).send_keys(password)
        self._BasePage__driver.find_element(*self.__login_button_locator).click()
        try:
            return InventoryPage(self._BasePage__driver)
        except:
            return self
        
    def get_error_message(self):
        return self._BasePage__driver.find_element(*self.__error_message_locator).text
