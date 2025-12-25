"""
   Методы работы с меню
"""
from page_factory.link import Link


class NavbarElement:
    def __init__(self, page):
        self.sign_out_button = Link(page, locator="//li[contains(text(), 'Sign out')]", name="Sign out")
        self.profile_link = Link(page, locator="[href='/profile']", name="Profile")

    def click_sign_out_button(self):
        self.sign_out_button.click()

    def click_profile_link(self):
        self.profile_link.click()
