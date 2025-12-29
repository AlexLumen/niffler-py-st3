import datetime
from random import choice

import pytest
from mimesis import Text, Finance

from clients.spends import SpendsHttpClient
from models.enums import CategoryEnum
from models.spend import SpendAdd, SpendEdit
from pages.add_spending_page import AddSpendingPage

finance = Finance()
text_generator = Text()


@pytest.fixture(scope="function")
def spend_data_for_add():
    return SpendAdd(
        amount=finance.price(),
        description=text_generator.sentence()[:40],
        category={"name": text_generator.word()},
        currency=choice(["KZT", "RUB", "EUR", "USD"]),
        spendDate=(datetime.datetime.now() - datetime.timedelta(days=1)).isoformat()
    )


@pytest.fixture(scope="function")
def add_spend(spends_client, spend_data_for_add, currency, delete_category_with_spendings):
    spend_data = {
        "amount": spend_data_for_add.amount,
        "description": spend_data_for_add.description,
        "category": spend_data_for_add.category,
        "spendDate": spend_data_for_add.spendDate,
        "currency": spend_data_for_add.currency

    }

    spend = spends_client.add_spends(spend_data)

    return spend


@pytest.fixture(scope="function")
def spend_data_for_edit():
    return SpendEdit(
        amount=finance.price(),
        description=text_generator.sentence()[:40],
        category={"name": text_generator.word()},
        currency=choice(["KZT", "RUB", "EUR", "USD"]),
        spendDate=(datetime.datetime.now() - datetime.timedelta(days=1)).isoformat()
    )


@pytest.fixture(scope="function")
def spends_client(envs, auth_token) -> SpendsHttpClient:
    return SpendsHttpClient(envs, auth_token)


@pytest.fixture
def currency():
    currencies_list_symbols = ["₸", "₽", "€", "$"]
    return choice(currencies_list_symbols)

@pytest.fixture
def category_value():
    return text_generator.word()

@pytest.fixture
def create_category(request, spends_client, category_db, category_value):
    category = spends_client.add_category(name=category_value)

    def teardown():
        category_db.delete_category(category.id)

    request.addfinalizer(teardown)
    return category


@pytest.fixture
def create_second_category(request, spends_client, category_db):
    category = spends_client.add_category(name=CategoryEnum.CATEGORY)

    def teardown():
        category_db.delete_category(category.id)

    request.addfinalizer(teardown)
    return category


@pytest.fixture
def add_spending_page(page):
    return AddSpendingPage(page)
