

import os
from page_factory.button import Button
from page_factory.paragraph import Paragraph
from page_factory.form import Form
from page_factory.input import Input
from page_factory.link import Link
from page_factory.title import Title
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_page_url = os.getenv('FRONT_URL')

        self.login_form = Form(page, locator="[action='/login']", name="Форма авторизации")
        self.title = Title(page, locator=".header", name="Заголовок страницы авторизации")
        self.user_name_field = Input(page, locator="[name='username']", name="Username")
        self.password_field = Input(page, locator="[name='password']", name="Password")
        self.login_button = Button(page, locator=".form__submit", name="Log in")
        self.new_account_button = Link(page, locator="[href='/register']", name="Create new account")
        self.error_message = Paragraph(page, locator=".form__error", name="Error message")

    def open_login_page(self):
        self.open_url(self.login_page_url)

    def check_visibility_login_form(self):
        self.login_form.should_be_visible()

    def send_user_name(self, user_name):
        self.user_name_field.fill(user_name)

    def send_password(self, password):
        self.password_field.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def check_login_button_visibility(self):
        self.login_button.should_be_visible()

    def click_create_new_account_button(self):
        self.new_account_button.click()

    def check_invalid_creds_error_message(self):
        self.error_message.should_have_text("Неверные учетные данные пользователя")
