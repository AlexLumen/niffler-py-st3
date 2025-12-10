import pytest

from Pages.ProfilePage import ProfilePage
from Pages.elements.ArchiveCategoryAlertElement import ArchiveCategoryAlertElement
from Pages.elements.HeaderElement import HeaderElement
from Pages.elements.NavbarElement import NavbarElement


@pytest.mark.usefixtures("open_profile_page", "archive_category")
def test_add_new_category(browser, category_value):
    pofile_page = ProfilePage(browser)
    pofile_page.send_category_name(category_value)
    pofile_page.press_enter_in_category_name()
    pofile_page.check_added_new_category(category_value)


@pytest.mark.usefixtures("open_profile_page")
def test_category_input_error_message_if_try_add_category_without_name(browser):
    pofile_page = ProfilePage(browser)
    pofile_page.press_enter_in_category_name()
    pofile_page.check_category_input_error_message()


@pytest.mark.usefixtures("login_user", "archive_category")
def test_edit_category(create_category, browser):
    pofile_page = ProfilePage(browser)
    navbar = NavbarElement(browser)
    header_element = HeaderElement(browser)
    header_element.click_person_icon()
    navbar.click_profile_link()
    pofile_page.click_edit_category_button()
    pofile_page.send_category_name_in_edit_input(create_category['name'])
    pofile_page.press_enter_in_edit_category_name()
    pofile_page.check_edited_category(create_category['name'])


@pytest.mark.usefixtures("login_user", "create_category")
def test_archive_category(browser):
    pofile_page = ProfilePage(browser)
    archive_alert = ArchiveCategoryAlertElement(browser)
    navbar = NavbarElement(browser)
    header_element = HeaderElement(browser)
    header_element.click_person_icon()
    navbar.click_profile_link()
    pofile_page.click_archive_category_button()
    archive_alert.click_archive_button()
    pofile_page.check_archived_category_not_visibility()


@pytest.mark.usefixtures("open_profile_page")
def test_edit_name(browser, user_data):
    pofile_page = ProfilePage(browser)
    pofile_page.send_name_in_name_input(user_data['first_name'])
    pofile_page.click_save_changes_button()
    pofile_page.check_success_edit_profile_message_visibility()
