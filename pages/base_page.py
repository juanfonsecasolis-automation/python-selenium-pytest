from selenium.webdriver.support.wait import WebDriverWait

class BasePage(object):

    explicitWaitTimeoutSeconds = 10

    def __init__(self, driver):
        self.driver = driver
        print('Calling BasePage constructor.')
        print(f'driver type is {type(driver)}')
        print(f'self.driver type is {type(self.driver)}')

    def verify_page_loaded_correctly(self):
        raise NotImplementedError()
    
    def find_element(self, locator):
        return self.driver.find_element(locator)
    
    def wait_until(self, condition):
        return WebDriverWait(self.driver, self.explicitWaitTimeoutSeconds).until(condition)