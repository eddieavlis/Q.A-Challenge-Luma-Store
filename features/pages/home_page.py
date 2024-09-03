from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://magento.softwaretestingboard.com/"

        # Localizadores dos elementos da página inicial
        self.search_box_locator = (By.CSS_SELECTOR, "input[title='Search']")
        self.cart_icon_locator = (By.XPATH, "//a[contains(@class,'action showcart')]")
        self.sign_in_button_locator = (By.XPATH, "//a[@title='Sign In']")

    def open(self):
        self.driver.get(self.url)

    def search_for_product(self, product_name):
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.search_box_locator)
        )
        search_box.clear()
        search_box.send_keys(product_name + Keys.RETURN)

    def click_cart_icon(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_icon_locator)
        ).click()

    def click_sign_in(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.sign_in_button_locator)
        ).click()
