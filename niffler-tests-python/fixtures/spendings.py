from random import choice

import pytest
from mimesis import Text, Finance

from clients.spends import SpendsHttpClient

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
    return text_generator.sentence()


@pytest.fixture
def currency():
    currencies_list_symbols = ["₸", "₽", "€", "$"]
    return choice(currencies_list_symbols)


@pytest.fixture
def create_category(spends_client, category_value):
    category = spends_client.add_category(name=category_value)
    return category
