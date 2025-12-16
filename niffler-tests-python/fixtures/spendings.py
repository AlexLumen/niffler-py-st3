from random import choice

import pytest
from mimesis import Text, Finance

from clients.spends import SpendsHttpClient
from pages.add_spending_page import AddSpendingPage

finance = Finance()
text_generator = Text()


@pytest.fixture(scope="function")
def spends_client(api_url, get_access_token) -> SpendsHttpClient:
    return SpendsHttpClient(api_url, get_access_token)


@pytest.fixture
def price_value():
    return finance.price()


@pytest.fixture
def category_value():
    return text_generator.word()


@pytest.fixture
def description_value():
    sentence = text_generator.sentence()
    return sentence[:40]


@pytest.fixture
def currency():
    currencies_list_symbols = ["₸", "₽", "€", "$"]
    return choice(currencies_list_symbols)


@pytest.fixture
def create_category(spends_client, category_value):
    category = spends_client.add_category(name=category_value)
    return category


@pytest.fixture
def add_spending_page(page):
    add_spending_page = AddSpendingPage(page)
    return add_spending_page
