"""
    Методы работы с окном подтверждения вылогина
"""
from page_factory.button import Button


class LogoutAlertElement:
    def __init__(self, page):
        self.logout_button = Button(page, locator="//button[contains(text(), 'Log out')]", name="Logout button")

    def click_logout_button(self):
        self.logout_button.click()
