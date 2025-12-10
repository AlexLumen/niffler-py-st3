"""
    Методы работы с главной страницей
"""
from playwright.sync_api import expect

from Pages.BasePage import BasePage



class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.history_spendings = browser[1].locator("[id='spendings']")
        self.no_spending_text = browser[1].locator("//p[contains(text(), 'There are no spendings')]")
        self.category_name = browser[1].locator(".MuiTableRow-root>.MuiTableCell-root:nth-child(2)>span")
        self.category_name_sell = browser[1].locator(".MuiTableRow-root>.MuiTableCell-root:nth-child(2)")
        self.amount_value = browser[1].locator('.MuiTableRow-root>.MuiTableCell-root:nth-child(3)>span')
        self.description_value = browser[1].locator('.MuiTableRow-root>.MuiTableCell-root:nth-child(4)>span')

    def check_spendings_block_visibility(self):
        """
         проверить отображение блока History of Spendings
        """
        expect(self.history_spendings).to_be_visible()

    def check_no_spends_text_visibility(self):
        """
         Проверить отображение текста There are no spendings
        """
        expect(self.no_spending_text).to_be_visible()

    def check_added_spend_visibility(self, expected_category, expected_amount):
        self.assertion_value_exist_in_list(self.category_name, expected_category)
        self.assertion_value_exist_in_list(self.amount_value, expected_amount)

    def check_spend_not_added(self, expected_category, expected_amount):
        if not self.is_element_present(self.no_spending_text):
            categories = self.category_name.all_text_contents()
            assert expected_category not in categories

            amounts = self.amount_value.all_text_contents()
            assert str(expected_amount).split(" ")[0] not in amounts

            # self.assertion_value_not_exist_in_list(*MainPageLocators.CATEGORY_NAME, expected_category)
            # self.assertion_value_not_exist_in_list(*MainPageLocators.AMOUNT_VALUE, expected_amount.split(" ")[0])

        else:
            expect(self.no_spending_text).to_be_visible()

    def get_id_attribute_created_spending(self, category_name):
        identify = self.get_element_attribute_from_list_by_text(self.category_name_sell, category_name, 'id')[
              24:]
        return identify
