import os

from Pages.BasePage import BasePage
from Pages.LoginPage.LoginPageLocators import LoginPageLocators


class LoginPage(BasePage):

    def check_visibility_login_form(self):
        self.verify_element_visibility(*LoginPageLocators.LOGIN_FORM)

    def send_user_name(self, user_name):
        self.send_text(*LoginPageLocators.USER_NAME_FIELD, user_name)

    def send_password(self, password):
        self.send_text(*LoginPageLocators.PASSWORD_FIELD, password)

    def click_login_button(self):
        self.click_element(*LoginPageLocators.LOGIN_BUTTON)

    def check_login_button_visibility(self):
        self.verify_element_visibility(*LoginPageLocators.LOGIN_BUTTON)

    def click_create_new_account_button(self):
        self.click_element(*LoginPageLocators.NEW_ACCOUNT_BUTTON)

    def check_invalid_creds_error_message(self):
        error_message = self.get_text(*LoginPageLocators.ERROR_MESSAGE)
        self.assertion(error_message, "Неверные учетные данные пользователя")
