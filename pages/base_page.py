class BasePage(object):

    __explicit_wait_timeout_seconds = 10
    base_url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        self.__driver = driver
        self._verify_page_loaded_correctly()

    def _verify_page_loaded_correctly(self):
        raise NotImplementedError()