"""
    Фикстура авторизации пользователя
"""
import pytest
from playwright.sync_api import Page

from Pages.LoginPage.LoginPage import LoginPage
from Pages.elements.HeaderElement.HeaderElement import HeaderElement
from Pages.elements.LogoutAlertElement.LogoutAlertElement import LogoutAlertElement
from Pages.elements.Navbar.NavbarElement import NavbarElement


@pytest.fixture(scope='function')
def login_user(request, user_creds, browser):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.send_user_name(user_creds['user_name'])
    login_page.send_password(user_creds['password'])
    login_page.click_login_button()

    return browser.evaluate("window.localStorage.getItem('id_token')")

    # def teardown():
    #     navbar = NavbarElement(browser)
    #     header_element = HeaderElement(browser)
    #     header_element.click_person_icon()
    #     navbar.click_sign_out_button()
    # request.addfinalizer(teardown)
