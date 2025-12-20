import pytest
import allure


@allure.feature("Страница Траты")
@allure.title("Отменить добавление траты")
@pytest.mark.usefixtures("login_user")
def test_cancel_add_spending(add_spending_page, main_page, header_element,
                             page, price_value, category_value, description_value):
    header_element.click_add_spending_button()
    add_spending_page.send_amount(price_value)
    add_spending_page.send_category(category_value)
    add_spending_page.send_description(description_value)
    add_spending_page.click_cancel_button()
    main_page.check_spend_not_added(category_value, price_value)


@allure.feature("Страница Траты")
@allure.title("Успешное добавление траты")
@pytest.mark.usefixtures("login_user", "delete_spending")
def test_success_add_spending(add_spending_page, page, main_page, header_element,
                              price_value, category_value, description_value, currency):
    header_element.click_add_spending_button()
    add_spending_page.send_amount(price_value)
    add_spending_page.send_category(category_value)
    add_spending_page.click_currency_select()
    add_spending_page.choose_currency_from_list(currency)
    add_spending_page.send_description(description_value)
    add_spending_page.click_add_button()
    main_page.check_added_spend_visibility(category_value, f"{price_value} {currency}")
    main_page.get_id_attribute_created_spending(category_value)


@allure.feature("Страница Траты")
@allure.title("Сообщение об ошибке при попытке добавить трату без суммы")
@pytest.mark.usefixtures("login_user")
def test_empty_amount_message_visibility_if_add_spending_without_amount(add_spending_page, page,
                                                                        category_value, description_value,
                                                                        header_element, currency):
    header_element.click_add_spending_button()
    add_spending_page.send_category(category_value)
    add_spending_page.click_currency_select()
    add_spending_page.choose_currency_from_list(currency)
    add_spending_page.send_description(description_value)
    add_spending_page.click_add_button()
    add_spending_page.check_empty_amount_message_visibility()


@allure.feature("Страница Траты")
@allure.title("Сообщение об ошибке при попытке добавить трату без категории")
@pytest.mark.usefixtures("login_user")
def test_empty_category_message_visibility_if_add_spending_without_category(add_spending_page,
                                                                            page, price_value, description_value,
                                                                            header_element, currency):
    header_element.click_add_spending_button()
    add_spending_page.send_amount(price_value)
    add_spending_page.click_currency_select()
    add_spending_page.choose_currency_from_list(currency)
    add_spending_page.send_description(description_value)
    add_spending_page.click_add_button()
    add_spending_page.check_empty_category_message_visibility()
