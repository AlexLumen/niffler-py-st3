from Pages.BasePage import BasePage
from Pages.RegistrationPage.RegistrationPageLocators import RegistrationPageLocators


class RegistrationPage(BasePage):

    def check_visibility_registration_from(self):
        self.verify_element_visibility(*RegistrationPageLocators.REGISTRATION_FORM)

    def send_username(self, username):
        self.send_text(*RegistrationPageLocators.USERNAME_INPUT, username)

    def send_password(self, password):
        self.send_text(*RegistrationPageLocators.PASSWORD_INPUT, password)

    def send_submit_password(self, password):
        self.send_text(*RegistrationPageLocators.SUBMIT_PASSWORD_INPUT, password)

    def click_sign_up_button(self):
        self.click_element(*RegistrationPageLocators.SIGN_UP_BUTTON)

    def check_success_registration_message(self):
        success_message = self.get_text(*RegistrationPageLocators.SUCCESS_REGISTRATION_MESSAGE)
        self.assertion(success_message, "Congratulations! You've registered!")

    def check_invalid_length_message_on_username_field(self):
        success_message = self.get_text(*RegistrationPageLocators.USERNAME_INPUT_ERROR_MESSAGE)
        self.assertion(success_message, "Allowed username length should be from 3 to 50 characters")

    def check_invalid_length_message_on_password_field(self):
        success_message = self.get_text(*RegistrationPageLocators.PASSWORD_INPUT_ERROR_MESSAGE)
        self.assertion(success_message, "Allowed password length should be from 3 to 12 characters")

    def check_invalid_length_message_on_submit_password_field(self):
        success_message = self.get_text(*RegistrationPageLocators.SUBMIT_PASSWORD_INPUT_ERROR_MESSAGE)
        self.assertion(success_message, "Allowed password length should be from 3 to 12 characters")

    def click_log_in_url(self):
        self.click_element(*RegistrationPageLocators.LOGIN_URL)

    def check_passwords_should_be_equal_message_on_password_field(self):
        success_message = self.get_text(*RegistrationPageLocators.PASSWORD_INPUT_ERROR_MESSAGE)
        self.assertion(success_message, "Passwords should be equal")

    def check_user_already_exist_on_username_field(self, username):
        success_message = self.get_text(*RegistrationPageLocators.USERNAME_INPUT_ERROR_MESSAGE)
        self.assertion(success_message, f"Username `{username}` already exists")

    def click_sign_in_button(self):
        self.click_element(*RegistrationPageLocators.SIGN_IN_BUTTON)
