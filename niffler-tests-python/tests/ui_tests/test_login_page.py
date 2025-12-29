"""
Тесты страницы авторизации
"""
import allure
import pytest


@allure.feature("Страница авторизации")
@allure.title("Успешная авторизация")
def test_success_login(page, main_page, envs, login_page):
    login_page.send_user_name(envs.username)
    login_page.send_password(envs.password)
    login_page.click_login_button()
    main_page.check_spendings_block_visibility()


@allure.feature("Страница авторизации")
@allure.title("Выход из аккаунта")
@pytest.mark.usefixtures("login_user")
def test_logout_user(page, login_page, logout_alert, header_element, navbar_element):
    header_element.click_person_icon()
    navbar_element.click_sign_out_button()
    logout_alert.click_logout_button()
    login_page.check_login_button_visibility()


@allure.feature("Страница авторизации")
@allure.title("Отображение сообщения о неправильном логине или пароле")
def test_error_message_visibility_when_invalid_creds_on_login(page, envs, login_page):
    login_page.send_user_name(envs.username)
    login_page.send_password("invalid_password")
    login_page.click_login_button()
    login_page.check_invalid_creds_error_message()


@allure.feature("Страница авторизации")
@allure.title("Переход на страницу регистрации со страницы авторизации")
def test_go_to_registration_page_from_login_page(login_page, registration_page, page):
    login_page.click_create_new_account_button()
    registration_page.check_visibility_registration_from()
