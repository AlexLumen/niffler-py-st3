# -*- coding: utf-8 -*-

"""
    Конфиг для тестов
"""
import os
from os import getenv
import pytest
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fixtures.authorization import *
from fixtures.person import *


@pytest.fixture(scope="session", autouse=True)
def envs():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    return {"url": os.getenv("FRONT_URL"),
            "user_name": os.getenv('USER_NAME'),
            "password": os.getenv('PASSWORD')}


@pytest.fixture(scope='function')
def browser(request):
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

    def open_browser(url="http://frontend.niffler.dc"):
        """
            Открыть браузер
        """
        return driver.get(url)

    driver.maximize_window()
    driver.open_browser = open_browser
    driver.open_browser()
    request.addfinalizer(driver.quit)

    return driver
