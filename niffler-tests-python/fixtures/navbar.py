import pytest

from components.navbar_element import NavbarElement


@pytest.fixture
def navbar_element(page):
    navbar_element = NavbarElement(page)
    return navbar_element
