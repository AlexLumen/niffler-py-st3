"""
    Фикстура авторизации пользователя
"""
import pytest

from pages.login_page import LoginPage


@pytest.fixture
def login_page(page):
    login_page = LoginPage(page)
    return login_page


@pytest.fixture(scope='function')
def login_user(request, envs, login_page, page, browser):
    login_page.open_login_page()
    login_page.send_user_name(envs.username)
    login_page.send_password(envs.password)
    login_page.click_login_button()
    context = browser.new_context(ignore_https_errors=True)
    context.storage_state(path="./user.json")

    return page.evaluate("window.localStorage.getItem('id_token')")
