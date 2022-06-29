from selenium.webdriver.common.by import By

class BasePageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    NOT_EMPTY_BASKET_BANNER = (By.CSS_SELECTOR, ".basket_summary")
    OPEN_BUSKET_BTN = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name ="registration_submit"]')

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, '.breadcrumb .active')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    MATCH_NAME = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) .alertinner:nth-child(2) > strong')
    MATCH_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert:nth-child(1) .alertinner:nth-child(2) ')
