import pytest
import allure


@allure.feature("Страница Траты")
@allure.title("Отменить добавление траты")
@pytest.mark.usefixtures("login_user")
def test_cancel_add_spending(add_spending_page, main_page, header_element,
                             page, spend_data_for_add):
    header_element.click_add_spending_button()
    add_spending_page.send_amount(spend_data_for_add.amount)
    add_spending_page.send_category(spend_data_for_add.category.name)
    add_spending_page.send_description(spend_data_for_add.description)
    add_spending_page.click_cancel_button()
    main_page.check_spend_not_added(spend_data_for_add.category.name, spend_data_for_add.amount)


@allure.feature("Страница Траты")
@allure.title("Успешное добавление траты")
@pytest.mark.usefixtures("login_user", "delete_spending")
def test_success_add_spending(add_spending_page, page, main_page, header_element,
                              currency, spend_data_for_add):
    header_element.click_add_spending_button()
    add_spending_page.send_amount(spend_data_for_add.amount)
    add_spending_page.send_category(spend_data_for_add.category.name)
    add_spending_page.click_currency_select()
    add_spending_page.choose_currency_from_list(currency)
    add_spending_page.send_description(spend_data_for_add.description)
    add_spending_page.click_add_button()
    main_page.check_added_spend_visibility(spend_data_for_add.category.name, f"{spend_data_for_add.amount} {currency}")
    main_page.get_id_attribute_created_spending(spend_data_for_add.category.name)


@allure.feature("Страница Траты")
@allure.title("Сообщение об ошибке при попытке добавить трату без суммы")
@pytest.mark.usefixtures("login_user")
def test_empty_amount_message_visibility_if_add_spending_without_amount(add_spending_page, page,
                                                                        header_element, currency, spend_data_for_add):
    header_element.click_add_spending_button()
    add_spending_page.send_category(spend_data_for_add.category.name)
    add_spending_page.click_currency_select()
    add_spending_page.choose_currency_from_list(currency)
    add_spending_page.send_description(spend_data_for_add.description)
    add_spending_page.click_add_button()
    add_spending_page.check_empty_amount_message_visibility()


@allure.feature("Страница Траты")
@allure.title("Сообщение об ошибке при попытке добавить трату без категории")
@pytest.mark.usefixtures("login_user")
def test_empty_category_message_visibility_if_add_spending_without_category(add_spending_page,
                                                                            page,
                                                                            header_element, currency,
                                                                            spend_data_for_add):
    header_element.click_add_spending_button()
    add_spending_page.send_amount(spend_data_for_add.amount)
    add_spending_page.click_currency_select()
    add_spending_page.choose_currency_from_list(currency)
    add_spending_page.send_description(spend_data_for_add.description)
    add_spending_page.click_add_button()
    add_spending_page.check_empty_category_message_visibility()
