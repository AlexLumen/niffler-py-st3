"""
    Фикстура авторизации пользователя
"""
import pytest

from pages.LoginPage import LoginPage


@pytest.fixture(scope='function')
def login_user(request, user_creds, browser):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.send_user_name(user_creds['user_name'])
    login_page.send_password(user_creds['password'])
    login_page.click_login_button()
    context = browser[0].new_context(ignore_https_errors=True)
    context.storage_state(path="./user.json")

    return browser[1].evaluate("window.localStorage.getItem('id_token')")
