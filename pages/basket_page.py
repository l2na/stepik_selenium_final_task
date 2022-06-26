from .locators import BasePageLocators
from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def element_is_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def element_is_not_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def should_be_empty_basket(self):
        assert self.element_is_not_present(*BasePageLocators.NOT_EMPTY_BASKET_BANNER), \
            "Basket is not empty, but should be"

    def should_be_empty_basket_message(self):
        assert self.element_is_present(*BasePageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is not present, but should be"
