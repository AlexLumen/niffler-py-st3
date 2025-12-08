from random import choice

import pytest
from mimesis import Text, Finance

finance = Finance()
text_generator = Text()


@pytest.fixture
def int_value():
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
