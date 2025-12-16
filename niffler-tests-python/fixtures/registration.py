import pytest

from pages.registration_page import RegistrationPage


@pytest.fixture
def registration_page(page):
    registration_page = RegistrationPage(page)
    return registration_page
