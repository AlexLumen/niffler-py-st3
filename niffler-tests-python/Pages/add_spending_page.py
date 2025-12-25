

from page_factory.button import Button
from page_factory.input import Input
from page_factory.paragraph import Paragraph
from page_factory.select import Select


class AddSpendingPage:
    def __init__(self, page):
        self.amount_field = Input(page, locator="[id='amount']", name="Amount")
        self.currency_select = Select(page, locator="[id='currency']", name="Currency")
        self.currency_item = Select(page, locator=".MuiPaper-root>.MuiList-padding>li>span:nth-child(1)",
                                    name="currency select item")
        self.category_field = Input(page, locator="[id='category']", name="Category")
        self.description_field = Input(page, locator="[id='description']", name="Description")
        self.cancel_button = Button(page, locator="[id='cancel']", name="Cancel")
        self.add_button = Button(page, locator="[id='save']", name="Add button")
        self.empty_amount_message = Paragraph(page, locator='Amount has to be not less then 0.01',
                                              name="Empty amount message", strategy="text")
        self.empty_category_message = Paragraph(page, locator='Please choose category',
                                                name="Choose category message", strategy="text")

    def send_amount(self, value):
        self.amount_field.fill(str(value))

    def click_currency_select(self):
        self.currency_select.click()

    def choose_currency_from_list(self, currency):
        self.currency_item.chose_element_in_list_by_text(currency)

    def send_category(self, value):
        self.category_field.fill(value)

    def send_description(self, value):
        self.description_field.fill(value)

    def click_cancel_button(self):
        self.cancel_button.click()

    def click_add_button(self):
        self.add_button.click()

    def check_empty_amount_message_visibility(self):
        self.empty_amount_message.should_be_visible()

    def check_empty_category_message_visibility(self):
        self.empty_category_message.should_be_visible()
