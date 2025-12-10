"""
    Методы работы с элементов Header
"""
from playwright.sync_api import Page

from Pages.BasePage import BasePage
from Pages.elements.HeaderElement.HeaderElementLocators import HeaderElementLocators


class HeaderElement(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.person_icon = browser.locator("[data-testid='PersonIcon']")
        self.add_spending_button = browser.locator("[href='/spending']")

    def click_person_icon(self):
        self.person_icon.click()

    def click_add_spending_button(self):
        self.add_spending_button.click()
