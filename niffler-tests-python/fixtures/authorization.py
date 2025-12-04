"""
    Фикстура авторизации пользователя
"""
import pytest

from Pages.LoginPage.LoginPage import LoginPage


@pytest.fixture(scope='function')
def login_user(browser, envs):
    login_page = LoginPage(browser)
    login_page.send_user_name(envs['user_name'])
    login_page.send_password(envs['password'])
    login_page.click_login_button()
