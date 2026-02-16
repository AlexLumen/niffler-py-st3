"""
    Методы работы с главной страницей
"""

from page_factory.paragraph import Paragraph
from page_factory.table_sell import TableSell
from page_factory.title import Title


class MainPage:
    def __init__(self, page):
        self.history_spendings_title = Title(page, locator='History of Spendings',
                                             name="History of Spendings title", strategy='text')
        self.no_spending_text = Paragraph(page, locator="There are no spendings",
                                          name="no spending text", strategy="text")
        self.category_name_sell = TableSell(page,
                                            locator=".MuiTableBody-root>.MuiTableRow-root>.MuiTableCell-root:nth"
                                                    "-child(2)",
                                            name="category name sell")
        self.amount_value_sell = TableSell(page,
                                           locator='.MuiTableBody-root>.MuiTableRow-root>.MuiTableCell-root:nth'
                                                   '-child(3)',
                                           name="amount sell")
        self.description_value_sell = TableSell(page,
                                                locator='.MuiTableBody-root>.MuiTableRow-root>.MuiTableCell-root:nth'
                                                        '-child(4)',
                                                name="description sell")


    def check_spendings_block_visibility(self):
        """
         проверить отображение блока History of Spendings
        """
        self.history_spendings_title.should_be_visible()

    def check_no_spends_text_visibility(self):
        """
         Проверить отображение текста There are no spendings
        """
        self.no_spending_text.should_be_visible()

    def check_added_spend_visibility(self, expected_category, expected_amount):
        self.category_name_sell.assertion_value_exist_in_list(expected_category)
        self.amount_value_sell.assertion_value_exist_in_list(expected_amount)

    def check_spend_not_added(self, expected_category, expected_amount):
        self.no_spending_text.should_be_visible()

    def get_id_attribute_created_spending(self, category_name):
        identify = self.category_name_sell.get_element_attribute_from_list_by_text(category_name, 'id')[
                   24:]
        return identify
