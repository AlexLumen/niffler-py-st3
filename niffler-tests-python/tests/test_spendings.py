import pytest

from Pages.AddSpendingPage import AddSpendingPage
from Pages.MainPage import MainPage
from Pages.elements.HeaderElement import HeaderElement
from helpers.currency import currencies


@pytest.mark.usefixtures("login_user")
def test_cancel_add_spending(browser, price_value, category_value, description_value):
    add_spending_page = AddSpendingPage(browser)
    header_element = HeaderElement(browser)
    main_page = MainPage(browser)
    header_element.click_add_spending_button()
    add_spending_page.send_amount(price_value)
    add_spending_page.send_category(category_value)
    add_spending_page.send_description(description_value)
    add_spending_page.click_cancel_button()
    main_page.check_spend_not_added(category_value, price_value)


@pytest.mark.usefixtures("login_user", "delete_spending")
def test_success_add_spending(envs, spend_db, browser, price_value, category_value, description_value, currency):
    add_spending_page = AddSpendingPage(browser)
    header_element = HeaderElement(browser)
    main_page = MainPage(browser)
    header_element.click_add_spending_button()
    add_spending_page.send_amount(price_value)
    add_spending_page.send_category(category_value)
    add_spending_page.click_currency_select()
    add_spending_page.choose_currency_from_list(currency)
    add_spending_page.send_description(description_value)
    add_spending_page.click_add_button()
    main_page.check_added_spend_visibility(category_value, f"{price_value} {currencies[currency]}")
    main_page.get_id_attribute_created_spending(category_value)
    spend_in_db = spend_db.get_spend_in_db(envs.username)
    assert spend_in_db[0].amount == price_value
    assert spend_in_db[0].description == description_value
    assert spend_in_db[0].currency == currency


@pytest.mark.usefixtures("login_user")
def test_empty_amount_message_visibility_if_add_spending_without_amount(browser, category_value, description_value,
                                                                        currency):
    add_spending_page = AddSpendingPage(browser)
    header_element = HeaderElement(browser)
    header_element.click_add_spending_button()
    add_spending_page.send_category(category_value)
    add_spending_page.click_currency_select()
    add_spending_page.choose_currency_from_list(currency)
    add_spending_page.send_description(description_value)
    add_spending_page.click_add_button()
    add_spending_page.check_empty_amount_message_visibility()


@pytest.mark.usefixtures("login_user")
def test_empty_category_message_visibility_if_add_spending_without_category(browser, price_value, description_value,
                                                                            currency):
    add_spending_page = AddSpendingPage(browser)
    header_element = HeaderElement(browser)
    header_element.click_add_spending_button()
    add_spending_page.send_amount(price_value)
    add_spending_page.click_currency_select()
    add_spending_page.choose_currency_from_list(currency)
    add_spending_page.send_description(description_value)
    add_spending_page.click_add_button()
    add_spending_page.check_empty_category_message_visibility()
