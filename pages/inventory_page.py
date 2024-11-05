from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage(BasePage):

    inventoryItemNameLocator = (By.XPATH, '//*[@data-test="inventory-item-name"]')

    def __init__(self, driver):
        super(InventoryPage, self).__init__(driver)

    def verify_page_loaded_correctly(self):
        assert "Swag Labs" in self.driver.title
        self.wait_until(EC.presence_of_element_located(self.inventoryItemNameLocator))
    