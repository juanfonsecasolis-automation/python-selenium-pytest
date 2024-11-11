from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage(BasePage):

    __inventoryItemNameLocator = By.XPATH, '//*[@data-test="inventory-item-name"]'

    def __init__(self, driver):
        super(InventoryPage, self).__init__(driver)

    def __verify_page_loaded_correctly(self):
        assert "Swag Labs" in self._BasePage__driver.title
        WebDriverWait(self._BasePage__driver, self._explicit_wait_timeout_seconds).until(EC.presence_of_element_located(*self.__inventoryItemNameLocator))
    