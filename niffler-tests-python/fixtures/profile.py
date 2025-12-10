import pytest

from Pages.ProfilePage import ProfilePage
from Pages.elements.HeaderElement import HeaderElement
from Pages.elements.NavbarElement import NavbarElement


@pytest.fixture
def open_profile_page(login_user, browser):
    navbar = NavbarElement(browser)
    header_element = HeaderElement(browser)
    header_element.click_person_icon()
    navbar.click_profile_link()


