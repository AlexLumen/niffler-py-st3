"""
    Фикстура авторизации пользователя
"""
import pytest
import sys
import os

# Добавляем путь к корневой директории
current_dir = os.path.dirname(__file__)
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture(scope='function')
def login_user(request, envs, login_page, page, browser):
    login_page.open_login_page()
    login_page.send_user_name(envs.username)
    login_page.send_password(envs.password)
    login_page.click_login_button()
    context = browser.new_context(ignore_https_errors=True)
    context.storage_state(path="./user.json")

    return page.evaluate("window.localStorage.getItem('id_token')")
