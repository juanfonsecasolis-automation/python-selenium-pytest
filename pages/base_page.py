class BasePage(object):

    __explicit_wait_timeout_seconds = 10
    base_url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        self.__driver = driver

    def __verify_page_loaded_correctly(self):
        raise NotImplementedError()