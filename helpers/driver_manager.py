from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

seconds_implicit_wait = None

def get_driver(browserType):

    driver = None
    if browserType=='Chrome':
        driverOptions = Options()
        driverOptions.add_argument('--headless')
        driver = webdriver.Chrome(
            options=driverOptions, 
            service=ChromeService(ChromeDriverManager().install()))
    else:
        raise NotImplementedError('Unknown webdriver.')
    
    if seconds_implicit_wait is not None:
        driver.implicitly_wait(seconds_implicit_wait) # seconds
    
    return driver