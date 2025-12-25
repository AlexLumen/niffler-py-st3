import pytest

from components.navbar_element import NavbarElement


@pytest.fixture
def navbar_element(page):
    return NavbarElement(page)
