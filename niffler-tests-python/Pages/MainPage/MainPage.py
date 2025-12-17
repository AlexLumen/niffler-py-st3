"""
    Методы работы с главной страницей
"""
from Pages.BasePage import BasePage
from Pages.MainPage.MainPageLocators import MainPageLocators


class MainPage(BasePage):

    def check_spendings_block_visibility(self):
        """
         проверить отображение блока History of Spendings
        """
        self.verify_element_visibility(*MainPageLocators.SPENDING)
