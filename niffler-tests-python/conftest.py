# -*- coding: utf-8 -*-

"""
    Конфиг для тестов
"""
import os
import time
from os import getenv
import pytest
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Pages.elements.HeaderElement.HeaderElement import HeaderElement
from Pages.elements.LogoutAlertElement.LogoutAlertElement import LogoutAlertElement
from Pages.elements.Navbar.NavbarElement import NavbarElement
from fixtures.authorization import *
from fixtures.person import *
from fixtures.spendings import *
from teadowns.spending import *


@pytest.fixture(scope="session")
def envs():
    load_dotenv()


@pytest.fixture(scope="session")
def frontend_url(envs):
    return os.getenv("FRONT_URL")


@pytest.fixture(scope="session")
def gateway_url(envs):
    return os.getenv("GATEWAY_URL")


@pytest.fixture(scope="session")
def app_user(envs):
    return os.getenv("USER_NAME"), os.getenv("PASSWORD")


@pytest.fixture(scope='session')
def browser(request, frontend_url):
    """Фикстура, открывающая браузер"""
    options = Options()

    options.add_argument("--start-maximized")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--incognito')
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument("--ignore-certificate-errors")

    driver = webdriver.Chrome(options=options)

    def open_browser(url=frontend_url):
        """
            Открыть браузер
        """
        return driver.get(url)

    driver.maximize_window()
    driver.open_browser = open_browser
    driver.open_browser()
    request.addfinalizer(driver.quit)

    return driver


@pytest.fixture(scope='session')
def login_user(browser, app_user):
    username, password = app_user
    login_page = LoginPage(browser)
    main_page = MainPage(browser)
    login_page.send_user_name(username)
    login_page.send_password(password)
    login_page.click_login_button()
    main_page.check_spendings_block_visibility()

    return browser.execute_script('return localStorage.getItem("id_token");')


@pytest.fixture(scope="function")
def logout(request, browser):
    def teardown():
        navbar = NavbarElement(browser)
        header_element = HeaderElement(browser)
        login_page = LoginPage(browser)
        logout_alert_element = LogoutAlertElement(browser)
        header_element.click_person_icon()
        navbar.click_sign_out_button()
        logout_alert_element.click_logout_button()
        login_page.check_login_button_visibility()

    request.addfinalizer(teardown)


@pytest.fixture(scope="function")
def auth_page(request, browser, frontend_url):
    def teardown():
        browser.get(frontend_url)

    request.addfinalizer(teardown)


@pytest.fixture()
def main_page(login_user, frontend_url):
    pass


@pytest.fixture(scope="session")
def spends_client(gateway_url, login_user) -> SpendsHttpClient:
    return SpendsHttpClient(gateway_url, login_user)
