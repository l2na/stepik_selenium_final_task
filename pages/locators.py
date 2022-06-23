from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, '.breadcrumb .active')
    MATCH_NAME = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) .alertinner:nth-child(2) > strong')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    MATCH_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert:nth-child(1) .alertinner:nth-child(2) ')
