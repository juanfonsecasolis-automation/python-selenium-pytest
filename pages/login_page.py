from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.inventory_page import InventoryPage

class LoginPage(BasePage):

    __usernameLocator = By.ID, 'user-name'
    __passwordLocator = By.ID, 'password'
    __loginButtonLocator = By.ID, 'login-button'

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def __verify_page_loaded_correctly(self):
        assert "Swag Labs" in self.__driver.title
        WebDriverWait(self.__driver, self._explicit_wait_timeout_seconds).until(EC.presence_of_element_located(*self.__loginButtonLocator))
    
    def login(self, username, password):
        self._BasePage__driver.find_element(*self.__usernameLocator).send_keys(username)
        self._BasePage__driver.find_element(*self.__passwordLocator).send_keys(password)
        self._BasePage__driver.find_element(*self.__loginButtonLocator).click()
        return InventoryPage(self._BasePage__driver)
