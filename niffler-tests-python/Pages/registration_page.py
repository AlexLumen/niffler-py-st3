
from page_factory.button import Button
from page_factory.form import Form
from page_factory.input import Input
from page_factory.link import Link
from page_factory.paragraph import Paragraph



class RegistrationPage:
    def __init__(self, page):
        self.registration_from = Form(page, locator="[id='register-form']", name="registration_form")
        self.username_input = Input(page, locator="[id='username']", name="Username")
        self.password_input = Input(page, locator="[id='password']", name="Password")
        self.submit_password_input = Input(page, locator="[id='passwordSubmit']", name="Submit password")
        self.submit_password_input_error_message = Paragraph(page, locator="xpath=//label[contains(text(), 'Submit "
                                                                           "password')]/span",
                                                             name="Passwords should be equal")
        self.sign_up_button = Button(page, locator="[type='submit']", name="Sign up")
        self.success_registration_message = Paragraph(page, locator=".form__paragraph_success",
                                                      name="Success registration message")
        self.login_url = Link(page, locator="Log in!", name="Log in", strategy="text")
        self.sign_in_button = Button(page, locator="Sign in", name="Sign in", strategy="text")
        self.username_input_error_message = Paragraph(page, locator="xpath=//label[contains(text(), 'Username')]/span",
                                                      name="Username error message")
        self.password_input_error_message = Paragraph(page, locator="xpath=//label[contains(text(), 'Password')]/span",
                                                      name="Password error message")

    def check_visibility_registration_from(self):
        self.registration_from.should_be_visible()

    def send_username(self, username):
        self.username_input.fill(username)

    def send_password(self, password):
        self.password_input.fill(password)

    def send_submit_password(self, password):
        self.submit_password_input.fill(password)

    def click_sign_up_button(self):
        self.sign_up_button.click()

    def check_success_registration_message(self):
        self.success_registration_message.should_have_text("Congratulations! You've registered!")

    def check_invalid_length_message_on_username_field(self):
        self.username_input_error_message.should_have_text(
            "Allowed username length should be from 3 to 50 characters")

    def check_invalid_length_message_on_password_field(self):
        self.password_input_error_message.should_have_text(
            "Allowed password length should be from 3 to 12 characters")

    def check_invalid_length_message_on_submit_password_field(self):
        self.submit_password_input_error_message.should_have_text(
            "Allowed password length should be from 3 to 12 characters")

    def click_log_in_url(self):
        self.login_url.click()

    def check_passwords_should_be_equal_message_on_password_field(self):
        self.password_input_error_message.should_have_text("Passwords should be equal")

    def check_user_already_exist_on_username_field(self, username):
        self.username_input_error_message.should_have_text(f"Username `{username}` already exists")

    def click_sign_in_button(self):
        self.sign_in_button.click()
