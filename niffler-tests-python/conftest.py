# -*- coding: utf-8 -*-

"""
    Конфиг для тестов
"""
import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Browser

from clients.kafka_client import KafkaClient
from clients.oauth_client import OAuthClient
from database.authority_db import AuthorityDb
from database.category_db import CategoriesDb
from database.spend_db import SpendDb
from database.user_db import UserDb

pytest_plugins = ["fixtures.authorization",
                  "fixtures.person",
                  "fixtures.spendings",
                  "fixtures.profile",
                  "fixtures.alerts",
                  "fixtures.header_element",
                  "fixtures.main_page",
                  "fixtures.navbar",
                  "fixtures.registration",
                  "fixtures.soap_fixtures",
                  "teadowns.spending",
                  "teadowns.categories"]

from models.config import Envs

import allure
from allure_commons.reporter import AllureReporter
from allure_commons.types import AttachmentType
from allure_pytest.listener import AllureListener
from pytest import Item, FixtureDef, FixtureRequest


@pytest.fixture(scope="session")
def envs():
    load_dotenv()
    envs_instance = Envs(frontend_url=os.getenv("FRONT_URL"),
                         gateway_url=os.getenv("GATEWAY_URL"),
                         auth_url=os.getenv("AUTH_URL"),
                         spend_db_url=os.getenv("SPEND_DB_URL"),
                         username=os.getenv('USER_NAME'),
                         password=os.getenv('PASSWORD'),
                         auth_db_url=os.getenv("AUTH_DB_URL"),
                         userdata_db_url=os.getenv("USERDATA_DB_URL"),
                         kafka_bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS")
                         )
    allure.attach(envs_instance.model_dump_json(indent=2), name="envs.json", attachment_type=AttachmentType.JSON)
    return envs_instance


@pytest.fixture(scope="session")
def spend_db(envs) -> SpendDb:
    return SpendDb(envs.spend_db_url)


@pytest.fixture(scope="session")
def category_db(envs) -> CategoriesDb:
    return CategoriesDb(envs.spend_db_url)


@pytest.fixture(scope="session")
def user_db(envs) -> UserDb:
    return UserDb(envs.userdata_db_url)


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
def pytest_runtest_call(item: pytest.Item):
    """
    Хук, срабатывающий при выполнении тела теста (после setup, перед teardown).
    Если тест падает — делаем скриншот и прикрепляем к Allure.
    """
    outcome = yield

    if outcome.excinfo is not None:
        page = item.funcargs.get("page")
        if page is not None and hasattr(page, "screenshot"):
            screenshot = page.screenshot()
            allure.attach(
                name="screenshotе",
                body=screenshot,
                attachment_type=allure.attachment_type.PNG
            )


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
    browser = playwright.chromium.launch(headless=True, args=["--start-fullscreen"])

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


@pytest.fixture(scope="session")
def auth_token(envs: Envs):
    print(envs.username)
    print(envs.password)
    return OAuthClient(envs).get_token(envs.username, envs.password)


@pytest.fixture(scope="session")
def auth_client(envs: Envs):
    return OAuthClient(envs)


@pytest.fixture(scope="session")
def kafka(envs):
    kafka_servers = envs.kafka_bootstrap_servers
    with KafkaClient(kafka_bootstrap_servers=kafka_servers) as k:
        yield k
