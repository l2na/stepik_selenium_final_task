from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    OPEN_BUSKET_BTN = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    NOT_EMPTY_BASKET_BANNER = (By.CSS_SELECTOR, ".basket_summary")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name ="registration_submit"]')

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, '.breadcrumb .active')
    MATCH_NAME = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) .alertinner:nth-child(2) > strong')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    MATCH_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert:nth-child(1) .alertinner:nth-child(2) ')
