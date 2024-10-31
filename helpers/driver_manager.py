from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def get_driver(browserType):
    if browserType=='Chrome':
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    else:
        raise Exception('Unknown webdriver.')