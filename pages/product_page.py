from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def go_to_basket_page(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        link.click()

    def book_name_match(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        match_name = self.browser.find_element(*ProductPageLocators.MATCH_NAME)
        assert book_name.text == match_name.text, "Book name doesn't match"

    def book_price_match(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        match_price = self.browser.find_element(*ProductPageLocators.MATCH_PRICE)
        assert book_price.text == match_price.text, "Book price doesn't match"













