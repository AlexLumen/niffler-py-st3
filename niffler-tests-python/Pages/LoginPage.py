import os

from playwright.sync_api import expect

from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.login_page_url = os.getenv('FRONT_URL')
        self.login_form = browser[1].locator("[action='/login']")
        self.title = browser[1].locator(".header")
        self.user_name_field = browser[1].locator("[name='username']")
        self.password_field = browser[1].locator("[name='password']")
        self.login_button = browser[1].locator(".form__submit")
        self.registration_url_button = browser[1].locator(".form__register")
        self.new_account_button = browser[1].locator("[href='/register']")
        self.error_message = browser[1].locator(".form__error")

    def open_login_page(self):
        self.open_url(self.login_page_url)

    def check_visibility_login_form(self):
        expect(self.login_form).to_be_visible()

    def send_user_name(self, user_name):
        self.user_name_field.fill(user_name)

    def send_password(self, password):
        self.password_field.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def check_login_button_visibility(self):
        expect(self.login_button).to_be_visible()

    def click_create_new_account_button(self):
        self.new_account_button.click()

    def check_invalid_creds_error_message(self):
        expect(self.error_message).to_contain_text("Неверные учетные данные пользователя")
