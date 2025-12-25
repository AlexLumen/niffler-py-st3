import pytest

from pages.profile_page import ProfilePage
from components.header_element import HeaderElement
from components.navbar_element import NavbarElement


@pytest.fixture
def profile_page(page):
    return ProfilePage(page)


@pytest.fixture
def open_profile_page(login_user, page):
    navbar = NavbarElement(page)
    header_element = HeaderElement(page)
    header_element.click_person_icon()
    navbar.click_profile_link()
