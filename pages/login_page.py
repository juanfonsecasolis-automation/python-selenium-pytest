from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    usernameLocator = By.ID, 'user-name'
    passwordLocator = By.ID, 'password'
    loginButtonLocator = By.ID, 'login-button'

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def verify_page_loaded_correctly(self):
        assert "Swag Labs" in self.driver.title
        WebDriverWait(self.driver, self.explicitWaitTimeoutSeconds).until(EC.presence_of_element_located(*self.loginButtonLocator))
    
    def login(self, username, password):
        self.driver.find_element(*self.usernameLocator).send_keys(username)
        self.driver.find_element(*self.passwordLocator).send_keys(password)
        self.driver.find_element(*self.loginButtonLocator).click()
