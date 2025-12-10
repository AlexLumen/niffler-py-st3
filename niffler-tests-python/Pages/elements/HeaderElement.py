"""
    Методы работы с элементов Header
"""

from Pages.BasePage import BasePage


class HeaderElement(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.person_icon = browser[1].locator("[data-testid='PersonIcon']")
        self.add_spending_button = browser[1].locator("[href='/spending']")

    def click_person_icon(self):
        self.person_icon.click()

    def click_add_spending_button(self):
        self.add_spending_button.click()
