# -*- coding: utf-8 -*-

"""
    Конфиг для тестов
"""
import os

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Browser
from fixtures.authorization import *
from fixtures.person import *
from fixtures.spendings import *
from fixtures.profile import *
from teadowns.spending import *


@pytest.fixture(scope="session")
def envs():
    load_dotenv()


@pytest.fixture(scope="session")
def frontend_url(envs):
    return os.getenv("FRONT_URL")


@pytest.fixture(scope="session")
def api_url(envs):
    return os.getenv("GATEWAY_URL")


@pytest.fixture(scope="session")
def auth_url(envs):
    return os.getenv("AUTH_URL")


@pytest.fixture(scope="session")
def user_creds(envs):
    return {
        'user_name': os.getenv('USER_NAME'),
        'password': os.getenv('PASSWORD'),
    }


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Запускать в headless‑режиме"
    )
    parser.addoption(
        "--no-headless",
        action="store_false",
        dest="headless",
        help="Запускать с GUI (отменяет --headless)"
    )


@pytest.fixture(scope="function")
def browser(request, frontend_url):
    """
    Фикстура, запускающая браузер через Playwright
    """
    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(
        headless=False,
        args=[

             ] + (["--start-fullscreen"]),
    )

    context = browser.new_context(ignore_https_errors=True)
    context.storage_state(path="./user.json")
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})

    def open_browser(url=frontend_url):
        page.goto(url, wait_until="domcontentloaded")

    page.open_browser = open_browser
    page.open_browser()

    def teardown():
        context.close()
        browser.close()
        playwright.stop()

    request.addfinalizer(teardown)

    return browser, page


@pytest.fixture(scope="function")
def page_with_auth(browser):
    """Страница с предустановленной авторизацией"""
    context = browser[0].new_context(storage_state="./niffler_user.json")
    page = context.new_page()

    yield page

    context.close()


@pytest.fixture(scope="function")
def get_access_token(browser):
    """
    Получить access_token из localStorage.

    Returns:
        str or None: Значение access_token или None, если не найден
    """
    token = browser[1].evaluate("window.localStorage.getItem('id_token')")
    return token
