from playwright.sync_api import expect

from pages.BasePage import BasePage


class AddSpendingPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.amount_field = browser[1].locator("[id='amount']")
        self.currency_select = browser[1].locator("[id='currency']")
        self.currency_item = browser[1].locator(".MuiPaper-root>.MuiList-padding>li>span:nth-child(2)")
        self.category_field = browser[1].locator("[id='category']")
        self.description_field = browser[1].locator("[id='description']")
        self.cancel_button = browser[1].locator("[id='cancel']")
        self.add_button = browser[1].locator("[id='save']")
        self.empty_amount_message = browser[1].get_by_text('Amount has to be not less then 0.01')
        self.empty_category_message = browser[1].get_by_text('Please choose category')

    def send_amount(self, value):
        self.amount_field.fill(str(value))

    def click_currency_select(self):
        self.currency_select.click()

    def choose_currency_from_list(self, currency):
        self.chose_element_in_list_by_text(self.currency_item, currency)

    def send_category(self, value):
        self.category_field.fill(value)

    def send_description(self, value):
        self.description_field.fill(value)

    def click_cancel_button(self):
        self.cancel_button.click()

    def click_add_button(self):
        self.add_button.click()

    def check_empty_amount_message_visibility(self):
        expect(self.empty_amount_message).to_be_visible()

    def check_empty_category_message_visibility(self):
        expect(self.empty_category_message).to_be_visible()
