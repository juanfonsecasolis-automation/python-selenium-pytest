from selenium.webdriver.support.wait import WebDriver, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):

    base_url = 'https://www.saucedemo.com/' # public member

    def __init__(self, driver: WebDriver):
        self._driver = driver   # protected member
        self._verify_page_loaded_correctly()

    def _verify_page_loaded_correctly(self):
        raise NotImplementedError()
    
    def _wait_until_element_is_visible(self, locator: tuple, timeout_seconds: int = 10):
        WebDriverWait(
            self._driver, 
            timeout_seconds
        ).until(
            EC.visibility_of_element_located(locator)
        )

    def _wait_until_element_contains_text(self, locator: tuple, expected_text: str, timeout_seconds: int = 10):
        WebDriverWait(
            self._driver, 
            timeout_seconds
        ).until(
            EC.text_to_be_present_in_element(locator, expected_text)
        )