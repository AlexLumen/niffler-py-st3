"""
    Тесты страницы регистрации
"""

import pytest
import allure


@allure.feature("Страница Регистрации")
@allure.title("Успешная регистрация")
def test_success_registration(login_page, registration_page, page, user_data):
    login_page.click_create_new_account_button()
    registration_page.send_username(user_data.username)
    registration_page.send_password(user_data.password)
    registration_page.send_submit_password(user_data.submit_password)
    registration_page.click_sign_up_button()
    registration_page.check_success_registration_message()


@allure.feature("Страница Регистрации")
@allure.title("Отображение сообщения об ошибке при вводе значений в поля недопустимое количество символов")
@pytest.mark.parametrize(
    "username, password, submit_password",
    [
        ("jo", "1s", "1s"),
        ("whis_username_have_length_51_symbols_it_is_very_lon",
         "whis_password_have_length_51_symbols_it_is_very_lon",
         "whis_password_have_length_51_symbols_it_is_very_lon")
    ]
)
def test_visibility_error_message_if_invalid_length_values(login_page, registration_page,
                                                           page, username, password, submit_password):
    login_page.click_create_new_account_button()
    registration_page.send_username(username)
    registration_page.send_password(password)
    registration_page.send_submit_password(submit_password)
    registration_page.click_sign_up_button()
    registration_page.check_invalid_length_message_on_username_field()
    registration_page.check_invalid_length_message_on_password_field()
    registration_page.check_invalid_length_message_on_submit_password_field()
    registration_page.click_log_in_url()


@allure.feature("Страница Регистрации")
@allure.title("Отображение сообщения об ошибке если пароли не совпадают")
def test_visibility_error_message_if_passwords_dont_match(login_page, registration_page, page, user_data):
    login_page.click_create_new_account_button()
    registration_page.send_username(user_data.username)
    registration_page.send_password(user_data.password)
    registration_page.send_submit_password("123")
    registration_page.click_sign_up_button()
    registration_page.check_passwords_should_be_equal_message_on_password_field()


@allure.feature("Страница Регистрации")
@allure.title("Отображение сообщения об ошибке если пользователь уже существует")
def test_visibility_error_message_when_user_is_existing(login_page, registration_page, page, envs):
    login_page.click_create_new_account_button()
    registration_page.send_username(envs.username)
    registration_page.send_password(envs.password)
    registration_page.send_submit_password(envs.password)
    registration_page.click_sign_up_button()
    registration_page.check_user_already_exist_on_username_field(envs.username)


@allure.feature("Страница Регистрации")
@allure.title("Переход на страницу авторизации со страницы регистрации")
def test_go_to_login_page_from_registration_page(login_page, registration_page, page):
    login_page.click_create_new_account_button()
    registration_page.click_log_in_url()
    login_page.check_visibility_login_form()


@allure.feature("Страница Регистрации")
@allure.title("Переход на страницу авторизации со страницы успешной регистрации")
def test_go_to_login_page_from_success_registration_page(login_page, registration_page, page, user_data):
    login_page.click_create_new_account_button()
    registration_page.send_username(user_data.username)
    registration_page.send_password(user_data.password)
    registration_page.send_submit_password(user_data.submit_password)
    registration_page.click_sign_up_button()
    registration_page.click_sign_in_button()
    login_page.check_visibility_login_form()
