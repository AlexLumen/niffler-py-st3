"""
    Методы работы с элементов Header
"""
from page_factory.button import Button
from page_factory.link import Link
from pages.base_page import BasePage


class HeaderElement(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.main_menu_button = Button(page, locator="[aria-label='Menu']", name="MainMenu")
        self.new_spending_button = Link(page, locator="[href='/spending']", name="New spending")

    def click_person_icon(self):
        self.main_menu_button.click()

    def click_add_spending_button(self):
        self.new_spending_button.click()
