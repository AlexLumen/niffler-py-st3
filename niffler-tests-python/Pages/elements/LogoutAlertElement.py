"""
    Методы работы с окном подтверждения вылогина
"""

from Pages.BasePage import BasePage


class LogoutAlertElement(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.logout_button = browser[1].locator("//button[contains(text(), 'Log out')]")

    def click_logout_button(self):
        self.logout_button.click()
