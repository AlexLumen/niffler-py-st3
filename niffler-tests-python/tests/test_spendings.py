

import pytest

from Pages.AddSpendingPage.AddSpendingPage import AddSpendingPage
from Pages.MainPage.MainPage import MainPage
from Pages.elements.HeaderElement.HeaderElement import HeaderElement


@pytest.mark.usefixtures("login_user")
def test_cancel_add_spending(browser, int_value, category_value, description_value):
    add_spending_page = AddSpendingPage(browser)
    header_element = HeaderElement(browser)
    main_page = MainPage(browser)
    header_element.click_add_spending_button()
    add_spending_page.send_amount(int_value)
    add_spending_page.send_category(category_value)
    add_spending_page.send_description(description_value)
    add_spending_page.click_cancel_button()
    main_page.check_spend_not_added(category_value, int_value)


@pytest.mark.usefixtures("login_user", "delete_spending")
def test_success_add_spending(browser, int_value, category_value, description_value, currency):
    add_spending_page = AddSpendingPage(browser)
    header_element = HeaderElement(browser)
    main_page = MainPage(browser)
    header_element.click_add_spending_button()
    add_spending_page.send_amount(int_value)
    add_spending_page.send_category(category_value)
    add_spending_page.click_currency_select()
    add_spending_page.choose_currency_from_list(currency)
    add_spending_page.send_description(description_value)
    add_spending_page.click_add_button()
    main_page.check_added_spend_visibility(category_value, f"{int_value} {currency}")
    main_page.get_id_attribute_created_spending(category_value)
