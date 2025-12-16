"""
Тесты страницы авторизации
"""
import pytest


def test_success_login(page, main_page, user_creds, login_page):
    login_page.send_user_name(user_creds.user_name)
    login_page.send_password(user_creds.password)
    login_page.click_login_button()
    main_page.check_spendings_block_visibility()


@pytest.mark.usefixtures("login_user")
def test_logout_user(page, login_page, logout_alert, header_element, navbar_element):
    header_element.click_person_icon()
    navbar_element.click_sign_out_button()
    logout_alert.click_logout_button()
    login_page.check_login_button_visibility()


def test_error_message_visibility_when_invalid_creds_on_login(page, user_creds, login_page):
    login_page.send_user_name(user_creds.user_name)
    login_page.send_password("invalid_password")
    login_page.click_login_button()
    login_page.check_invalid_creds_error_message()


def test_go_to_registration_page_from_login_page(login_page, registration_page, page):
    login_page.click_create_new_account_button()
    registration_page.check_visibility_registration_from()
