from selenium.webdriver.support.wait import WebDriver

class BasePage(object):

    _explicit_wait_timeout_seconds = 10 # protected member?
    base_url = 'https://www.saucedemo.com/' # public member

    def __init__(self, driver: WebDriver):
        self._driver = driver   # protected member?
        self._verify_page_loaded_correctly()

    def _verify_page_loaded_correctly(self):
        raise NotImplementedError()