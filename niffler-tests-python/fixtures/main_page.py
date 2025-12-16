import pytest

from pages.main_page import MainPage


@pytest.fixture
def main_page(page):
    main_page = MainPage(page)
    return main_page
