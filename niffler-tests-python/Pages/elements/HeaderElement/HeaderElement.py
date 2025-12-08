"""
    Методы работы с элементов Header
"""

from Pages.BasePage import BasePage
from Pages.elements.HeaderElement.HeaderElementLocators import HeaderElementLocators


class HeaderElement(BasePage):

    def click_person_icon(self):
        self.click_element(*HeaderElementLocators.PERSON_ICON)

    def click_add_spending_button(self):
        self.click_element(*HeaderElementLocators.ADD_SPENDING_BUTTON)
