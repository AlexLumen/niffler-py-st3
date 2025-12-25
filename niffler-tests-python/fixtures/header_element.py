import pytest

from components.header_element import HeaderElement


@pytest.fixture
def header_element(page):
    return HeaderElement(page)
