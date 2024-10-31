import pytest
from selenium.webdriver.common.by import By
from helpers.driver_manager import get_driver

class TestLogin:

    @pytest.fixture()
    def driver(self, params):
        self.driver = get_driver(params['browser'])
        self.driver.get("https://www.saucedemo.com/")
        yield
        self.driver.close()

    @pytest.mark.positiveTests
    def test_positive_login(self, driver):
        assert "Swag Labs" in self.driver.title
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        assert "Products" not in self.driver.page_source

    @pytest.mark.negativeTests
    def test_negative_login(self, driver):
        assert "Swag Labs" in self.driver.title
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        assert "Products" not in self.driver.page_source