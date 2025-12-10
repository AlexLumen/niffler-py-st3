from Pages.AddSpendingPage.AddSpendingPageLocators import AddSpendingPageLocators
from Pages.BasePage import BasePage


class AddSpendingPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.amount_field = browser.locator("[id='amount']")
        self.currency_select = browser.locator("[id='currency']")
        self.currency_item = browser.locator(".MuiPaper-root>.MuiList-padding>li>span:nth-child(1)")
        self.category_field = browser.locator("[id='category']")
        self.description_field = browser.locator("[id='description']")
        self.cancel_button = browser.locator("[id='cancel']")
        self.add_button = browser.locator("[id='save']")

    def send_amount(self, value):
        self.amount_field.fill(str(value))

    def click_currency_select(self):
        self.currency_select.click()

    def choose_currency_from_list(self, currency):
        self.chose_element_in_list_by_text(self.currency_item, currency)



       # self.chose_element_in_list_by_text(self.currency_item, currency)

    def send_category(self, value):
        self.category_field.fill(value)

    def send_description(self, value):
        self.description_field.fill(value)

    def click_cancel_button(self):
        self.cancel_button.click()

    def click_add_button(self):
        self.add_button.click()
