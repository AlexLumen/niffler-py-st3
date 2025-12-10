"""
   Методы работы с меню
"""
from playwright.sync_api import Page

from Pages.elements.Navbar.NavbarElementLocators import NavbarElementLocators
from Pages.BasePage import BasePage


class NavbarElement(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.sign_out_button = browser.locator("//li[contains(text(), 'Sign out')]")

    def click_sign_out_button(self):
        self.sign_out_button.click()
