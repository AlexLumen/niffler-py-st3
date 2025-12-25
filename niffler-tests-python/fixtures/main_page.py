import pytest

from pages.main_page import MainPage


@pytest.fixture
def main_page(page):
    return MainPage(page)
