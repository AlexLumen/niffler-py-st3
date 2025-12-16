# -*- coding: utf-8 -*-

"""
    Конфиг для тестов
"""
import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Browser
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
from models.user_auth import UserAuth
from teadowns.spending import delete_spending, archive_category


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
    return UserAuth(user_name=os.getenv('USER_NAME'), password=os.getenv('PASSWORD'))


def pytest_addoption(parser):
    parser.addoption(
        "--headless"
    )
    parser.addoption(
        "--no-headless"
    )


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
def page(browser, frontend_url):
    context = browser.new_context(ignore_https_errors=True)
    context.storage_state(path="./user.json")
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})

    def open_browser(url=frontend_url):
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
