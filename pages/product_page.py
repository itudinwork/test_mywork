from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
class PageObject(BasePage):

    def add_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button_basket.click()

    def product_name(self):
        return self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text

    def product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text

    def basket_product_name(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_NAME_PRODUCT).text

    def basket_product_price(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_PRICE_PRODUCT).text


    def product_verification(self):
        assert self.product_name() == self.basket_product_name(), "error_name"
        assert self.product_price() == self.basket_product_price(), "error_price"
