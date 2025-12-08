"""
    Методы работы с окном подтверждения вылогина
"""
from Pages.BasePage import BasePage
from Pages.elements.LogoutAlertElement.LogoutAlertElementLocators import LogoutAlertElementLocators


class LogoutAlertElement(BasePage):

    def click_logout_button(self):
        self.click_element(*LogoutAlertElementLocators.LOGOUT_BUTTON)