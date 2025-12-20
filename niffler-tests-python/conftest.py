# -*- coding: utf-8 -*-

"""
    Конфиг для тестов
"""
import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Browser

from database.authority_db import AuthorityDb
from database.category_db import CategoriesDb
from database.spend_db import SpendDb
from database.user_db import UserDb
from fixtures.authorization import login_user, login_page
from fixtures.person import person_generator, user_data
from fixtures.spendings import (spends_client, price_value, category_value,
                                description_value, currency, create_category, add_spending_page)
from fixtures.profile import open_profile_page, profile_page
from fixtures.alerts import archive_category_alert, logout_alert
from fixtures.header_element import header_element
from fixtures.main_page import main_page
from fixtures.navbar import navbar_element
from fixtures.registration import registration_page
from models.config import Envs
from models.user_auth import UserAuth
from teadowns.spending import delete_spending, archive_category
import allure
from allure_commons.reporter import AllureReporter
from allure_commons.types import AttachmentType
from allure_pytest.listener import AllureListener
from pytest import Item, FixtureDef, FixtureRequest


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
        "--headless"
    )
    parser.addoption(
        "--no-headless"
    )


def allure_logger(config) -> AllureReporter:
    listener: AllureListener = config.pluginmanager.get_plugin("allure_listener")
    return listener.allure_logger


@pytest.hookimpl(hookwrapper=True, trylast=True)
def pytest_runtest_call(item: Item):
    yield


# allure.dynamic.title(" ".join(item.name.split("_")[1:]).title())


@pytest.hookimpl(hookwrapper=True, trylast=True)
def pytest_fixture_setup(fixturedef: FixtureDef, request: FixtureRequest):
    yield
    logger = allure_logger(request.config)
    item = logger.get_last_item()
    scope_letter = fixturedef.scope[0].upper()
    item.name = f"[{scope_letter}] " + " ".join(fixturedef.argname.split("_")).title()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_teardown(item):
    yield
    reporter = allure_logger(item.config)
    test = reporter.get_test(None)
    test.labels = list(filter(lambda x: x.name not in ("suite", "subSuite", "parentSuite"), test.labels))


@pytest.fixture(scope="function")
def browser(request):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, args=["--start-fullscreen"])

    def teardown():
        browser.close()
        playwright.stop()

    request.addfinalizer(teardown)
    return browser


@pytest.fixture(scope="function")
def page(browser, envs):
    context = browser.new_context(ignore_https_errors=True)
    context.storage_state(path="./user.json")
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})

    def open_browser(url=envs.frontend_url):
        page.goto(url, wait_until="domcontentloaded")

    page.open_browser = open_browser
    page.open_browser()

    return page


@pytest.fixture(scope="function")
def get_access_token(page):
    """
    Получить access_token из localStorage.

    Returns:
        str or None: Значение access_token или None, если не найден
    """
    token = page.evaluate("window.localStorage.getItem('id_token')")
    return token
