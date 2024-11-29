#
# Copyright November 2024 Juan M. Fonseca-Solís.
# Pytest/Selenium minimum working example (MWE).
# Reference: https://www.udemy.com/certificate/UC-36a2f5ef-d733-4d5d-964f-481c55e320e8 (certificate).
#

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_driver(params: dict):

    driver = None
    if params['browser']=='Chrome':
        driverOptions = Options()
        if params['headless']=='True':
            driverOptions.add_argument('--headless')
        driver = webdriver.Chrome(
            options=driverOptions, 
            service=ChromeService(ChromeDriverManager().install()))
    else:
        raise NotImplementedError('Unknown webdriver.')
    
    # Do not use implicit wait along explicit wait (there should be no calls to explicit waits in the code)
    # seconds_implicit_wait = 5
    # driver.implicitly_wait(seconds_implicit_wait) # seconds
    
    return driver