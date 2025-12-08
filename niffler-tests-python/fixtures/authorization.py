"""
    Фикстура авторизации пользователя
"""
import pytest

from Pages.LoginPage.LoginPage import LoginPage


@pytest.fixture(scope='session')
def login_user(browser, app_user):
    username, password = app_user
    login_page = LoginPage(browser)
    login_page.send_user_name(username)
    login_page.send_password(password)
    login_page.click_login_button()
