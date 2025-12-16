import pytest

from components.header_element import HeaderElement


@pytest.fixture
def header_element(page):
    header_element = HeaderElement(page)
    return header_element
