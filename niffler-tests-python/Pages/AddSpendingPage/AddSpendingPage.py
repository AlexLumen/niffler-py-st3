from Pages.AddSpendingPage.AddSpendingPageLocators import AddSpendingPageLocators
from Pages.BasePage import BasePage


class AddSpendingPage(BasePage):

    def send_amount(self, value):
        self.send_text(*AddSpendingPageLocators.AMOUNT_FIELD, value)

    def click_currency_select(self):
        self.click_element(*AddSpendingPageLocators.CURRENCY_SELECT)

    def choose_currency_from_list(self, currency):
        self.chose_element_in_list_by_text(*AddSpendingPageLocators.CURRENCY_ITEM, currency)

    def send_category(self, value):
        self.send_text(*AddSpendingPageLocators.CATEGORY_FIELD, value)

    def send_description(self, value):
        self.send_text(*AddSpendingPageLocators.DESCRIPTION_FIELD, value)

    def click_cancel_button(self):
        self.click_element(*AddSpendingPageLocators.CANCEL_BUTTON)

    def click_add_button(self):
        self.click_element(*AddSpendingPageLocators.ADD_BUTTON)
