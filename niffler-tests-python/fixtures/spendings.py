from random import choice

import pytest
from mimesis import Text, Finance

from clients.spends import SpendsHttpClient

finance = Finance()
text_generator = Text()


@pytest.fixture(scope="function")
def spends_client(envs, get_access_token) -> SpendsHttpClient:
    return SpendsHttpClient(envs.gateway_url, get_access_token)


@pytest.fixture
def price_value():
    return finance.price()


@pytest.fixture
def category_value():
    return text_generator.word()


@pytest.fixture
def category_value_edited():
    return text_generator.word()

@pytest.fixture
def description_value():
    return text_generator.sentence()


@pytest.fixture
def currency():
    currencies_list = ["RUB", "KZT", "EUR", "USD"]
    return choice(currencies_list)


@pytest.fixture
def create_category(request, spends_client, category_value, category_db, envs):
    category = spends_client.add_category(name=category_value)

    def teardown():
        category_db.delete_category(category['id'])

    request.addfinalizer(teardown)
    return category
