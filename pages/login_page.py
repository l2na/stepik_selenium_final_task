from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.email = self.browser.find_element(*LoginPageLocators.EMAIL_FORM)
        self.email.send_keys(email)
        self.password = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM)
        self.password.send_keys(password)
        self.password2 = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD)
        self.password2.send_keys(password)
        self.register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True
