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

    def check_no_spends_text_visibility(self):
        """
         Проверить отображение текста There are no spendings
        """
        self.verify_element_visibility(*MainPageLocators.NO_SPENDING_TEXT)

    def check_added_spend_visibility(self, expected_category, expected_amount):
        self.assertion_value_exist_in_list(*MainPageLocators.CATEGORY_NAME, expected_category)
        self.assertion_value_exist_in_list(*MainPageLocators.AMOUNT_VALUE, expected_amount)

    def check_spend_not_added(self, expected_category, expected_amount):
        print("is ",self.is_element_present(*MainPageLocators.NO_SPENDING_TEXT))
        if not self.is_element_present(*MainPageLocators.NO_SPENDING_TEXT):
            self.assertion_value_not_exist_in_list(*MainPageLocators.CATEGORY_NAME, expected_category)
            self.assertion_value_not_exist_in_list(*MainPageLocators.AMOUNT_VALUE, expected_amount.split(" ")[0])

        else:
            self.verify_element_visibility(*MainPageLocators.NO_SPENDING_TEXT)

    def get_id_attribute_created_spending(self, category_name):
        identify = self.get_element_attribute_from_list_by_text(*MainPageLocators.CATEGORY_NAME_SELL, category_name, 'id')[
              24:]
        return identify

