"""
   Методы работы с меню
"""

from Pages.elements.Navbar.NavbarElementLocators import NavbarElementLocators
from Pages.BasePage import BasePage


class NavbarElement(BasePage):

    def click_sign_out_button(self):
        self.click_element(*NavbarElementLocators.SIGN_OUT_BUTTON)
