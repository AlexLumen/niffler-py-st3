"""
    Методы работы с окном подтверждения вылогина
"""
from playwright.sync_api import Page

from Pages.BasePage import BasePage
from Pages.elements.LogoutAlertElement.LogoutAlertElementLocators import LogoutAlertElementLocators


class LogoutAlertElement(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.logout_button = browser.locator("//button[contains(text(), 'Log out')]")

    def click_logout_button(self):
        self.logout_button.click()
