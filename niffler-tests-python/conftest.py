# -*- coding: utf-8 -*-

"""
    Конфиг для тестов
"""
import os

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Browser

from database.authority_db import AuthorityDb
from database.category_db import CategoriesDb
from database.spend_db import SpendDb
from database.user_db import UserDb
from fixtures.authorization import *
from fixtures.person import *
from fixtures.spendings import *
from fixtures.profile import *
from models.config import Envs
from teadowns.spending import *
from teadowns.categories import *
from teadowns.users import *


@pytest.fixture(scope="session")
def envs() -> Envs:
    load_dotenv()
    return Envs(frontend_url=os.getenv("FRONT_URL"),
                gateway_url=os.getenv("GATEWAY_URL"),
                auth_url=os.getenv("AUTH_URL"),
                spend_db_url=os.getenv("SPEND_DB_URL"),
                username=os.getenv('USER_NAME'),
                password=os.getenv('PASSWORD'),
                auth_db_url=os.getenv("AUTH_DB_URL")
                )


@pytest.fixture(scope="session")
def user_creds(envs):
    return {
        'user_name': envs.username,
        'password': envs.password,
    }


@pytest.fixture(scope="session")
def spend_db(envs) -> SpendDb:
    return SpendDb(envs.spend_db_url)


@pytest.fixture(scope="session")
def category_db(envs) -> CategoriesDb:
    return CategoriesDb(envs.spend_db_url)


@pytest.fixture(scope="session")
def user_db(envs) -> UserDb:
    return UserDb(envs.auth_db_url)


@pytest.fixture(scope="session")
def authority_db(envs) -> AuthorityDb:
    return AuthorityDb(envs.auth_db_url)


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
def browser(request, envs):
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

    def open_browser(url=envs.frontend_url):
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
