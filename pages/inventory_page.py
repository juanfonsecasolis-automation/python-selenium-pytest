from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage(BasePage):

    inventoryItemNameLocator = (By.XPATH, '//*[@data-test="inventory-item-name"]')

    def __init__(self, driver):
        super().__init__(driver)

    def verify_page_loaded_correctly(self):
        assert "Swag Labs" in self.driver.title
        WebDriverWait(self.driver, self.explicitWaitTimeoutSeconds).until(EC.presence_of_element_located(self.inventoryItemNameLocator))
    