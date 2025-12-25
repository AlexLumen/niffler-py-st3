import pytest

from pages.registration_page import RegistrationPage


@pytest.fixture
def registration_page(page):
    return RegistrationPage(page)
