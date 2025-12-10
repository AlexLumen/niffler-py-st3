"""
Тесты страницы авторизации
"""
import pytest
from dotenv import load_dotenv

from Pages.LoginPage.LoginPage import LoginPage
from Pages.MainPage.MainPage import MainPage
from Pages.RegistrationPage.RegistrationPage import RegistrationPage
from Pages.elements.HeaderElement.HeaderElement import HeaderElement
from Pages.elements.LogoutAlertElement.LogoutAlertElement import LogoutAlertElement
from Pages.elements.Navbar.NavbarElement import NavbarElement


def test_success_login(browser, user_creds):
    login_page = LoginPage(browser)
    main_page = MainPage(browser)
    login_page.send_user_name(user_creds['user_name'])
    login_page.send_password(user_creds['password'])
    login_page.click_login_button()
    main_page.check_spendings_block_visibility()


@pytest.mark.usefixtures("login_user")
def test_logout_user(browser):
    navbar = NavbarElement(browser)
    header_element = HeaderElement(browser)
    login_page = LoginPage(browser)
    logout_alert_element = LogoutAlertElement(browser)
    header_element.click_person_icon()
    navbar.click_sign_out_button()
    logout_alert_element.click_logout_button()
    login_page.check_login_button_visibility()


def test_error_message_visibility_when_invalid_creds_on_login(browser, user_creds):
    login_page = LoginPage(browser)
    login_page.send_user_name(user_creds['user_name'])
    login_page.send_password("invalid_password")
    login_page.click_login_button()
    login_page.check_invalid_creds_error_message()


def test_go_to_registration_page_from_login_page(browser):
    login_page = LoginPage(browser)
    registration_page = RegistrationPage(browser)
    login_page.click_create_new_account_button()
    registration_page.check_visibility_registration_from()
