class BasePage(object):

    explicitWaitTimeoutSeconds = 10

    def __init__(self, driver):
        self.driver = driver

    def _verify_page_loaded_correctly(self):
        raise NotImplementedError()