from playwright.sync_api import expect

from Pages.BasePage import BasePage


class RegistrationPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.registration_from = browser[1].locator("[id='register-form']")
        self.username_input = browser[1].locator("[id='username']")
        self.password_input = browser[1].locator("[id='password']")
        self.submit_password_input = browser[1].locator("[id='passwordSubmit']")
        self.submit_password_input_error_message = browser[1].locator("//label[contains(text(), 'Submit password')]/span")
        self.sign_up_button = browser[1].locator("[type='submit']")
        self.success_registration_message = browser[1].locator(".form__paragraph_success")
        self.login_url = browser[1].get_by_text("Log in!")
        self.sign_in_button = browser[1].get_by_text("Sign in")
        self.username_input_error_message = browser[1].locator("//label[contains(text(), 'Username')]/span")
        self.password_input_error_message = browser[1].locator("//label[contains(text(), 'Password')]/span")

    def check_visibility_registration_from(self):
        expect(self.registration_from).to_be_visible()

    def send_username(self, username):
        self.username_input.fill(username)

    def send_password(self, password):
        self.password_input.fill(password)

    def send_submit_password(self, password):
        self.submit_password_input.fill(password)

    def click_sign_up_button(self):
        self.sign_up_button.click()

    def check_success_registration_message(self):
        expect(self.success_registration_message).to_contain_text("Congratulations! You've registered!")

    def check_invalid_length_message_on_username_field(self):
        expect(self.username_input_error_message).to_contain_text(
            "Allowed username length should be from 3 to 50 characters")

    def check_invalid_length_message_on_password_field(self):
        expect(self.password_input_error_message).to_contain_text(
            "Allowed password length should be from 3 to 12 characters")

    def check_invalid_length_message_on_submit_password_field(self):
        expect(self.submit_password_input_error_message).to_contain_text(
            "Allowed password length should be from 3 to 12 characters")

    def click_log_in_url(self):
        self.login_url.click()

    def check_passwords_should_be_equal_message_on_password_field(self):
        expect(self.password_input_error_message).to_contain_text("Passwords should be equal")

    def check_user_already_exist_on_username_field(self, username):
        expect(self.username_input_error_message).to_contain_text(f"Username `{username}` already exists")

    def click_sign_in_button(self):
        self.sign_in_button.click()
