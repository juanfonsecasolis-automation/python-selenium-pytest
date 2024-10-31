class BasePage(object):

    explicitWaitTimeoutSeconds = 10
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def verify_page_loaded_correctly(self):
        raise NotImplementedError()