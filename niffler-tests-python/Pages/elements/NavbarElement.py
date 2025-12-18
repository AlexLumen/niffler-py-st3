"""
   Методы работы с меню
"""
from pages.BasePage import BasePage


class NavbarElement(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.sign_out_button = browser[1].locator("//li[contains(text(), 'Sign out')]")
        self.profile_link = browser[1].locator("[href='/profile']")

    def click_sign_out_button(self):
        self.sign_out_button.click()

    def click_profile_link(self):
        self.profile_link.click()
