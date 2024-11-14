from pages.with_upper_menu_page import WithUpperMenuPage
from selenium.webdriver.support.wait import WebDriverWait, WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage(WithUpperMenuPage):

    __inventoryItemNameLocator = (By.XPATH, '//*[@data-test="inventory-item-name"]')  # private attribute

    def __init__(self, driver: WebDriver):
        super(InventoryPage, self).__init__(driver)

    def _verify_page_loaded_correctly(self):
        assert "/inventory.html" in self._driver.current_url
        WebDriverWait(
            self._driver, 
            self._explicit_wait_timeout_seconds
        ).until(
            EC.presence_of_element_located(self.__inventoryItemNameLocator)
        )
    