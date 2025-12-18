import pytest

from pages.ProfilePage import ProfilePage
from pages.elements.ArchiveCategoryAlertElement import ArchiveCategoryAlertElement
from pages.elements.HeaderElement import HeaderElement
from pages.elements.NavbarElement import NavbarElement


@pytest.mark.usefixtures("open_profile_page", "delete_category")
def test_add_new_category(browser, category_value, envs, category_db):
    pofile_page = ProfilePage(browser)
    pofile_page.send_category_name(category_value)
    pofile_page.press_enter_in_category_name()
    pofile_page.check_added_new_category(category_value)
    category_in_db = category_db.get_category_by_name(envs.username, category_value)
    assert category_in_db.name == category_value


@pytest.mark.usefixtures("open_profile_page")
def test_category_input_error_message_if_try_add_category_without_name(browser):
    pofile_page = ProfilePage(browser)
    pofile_page.press_enter_in_category_name()
    pofile_page.check_category_input_error_message()


@pytest.mark.usefixtures("login_user")
def test_edit_category(envs, create_category, category_db, browser):
    pofile_page = ProfilePage(browser)
    navbar = NavbarElement(browser)
    header_element = HeaderElement(browser)
    header_element.click_person_icon()
    navbar.click_profile_link()
    pofile_page.click_edit_category_button()
    pofile_page.send_category_name_in_edit_input(create_category['name'])
    pofile_page.press_enter_in_edit_category_name()

    pofile_page.check_edited_category(f"{create_category['name']}")
    category_in_db = category_db.get_category_by_id(create_category['id'])

    assert category_in_db.name == f"{create_category['name']}_edited"


@pytest.mark.usefixtures("login_user", "create_category")
def test_archive_category(browser, category_db, envs, category_value):
    pofile_page = ProfilePage(browser)
    archive_alert = ArchiveCategoryAlertElement(browser)
    navbar = NavbarElement(browser)
    header_element = HeaderElement(browser)
    header_element.click_person_icon()
    navbar.click_profile_link()
    pofile_page.click_archive_category_button()
    archive_alert.click_archive_button()
    pofile_page.check_archived_category_not_visibility()
    category_in_db = category_db.get_category_by_name(envs.username, category_value)

    assert category_in_db.archived is True


@pytest.mark.usefixtures("open_profile_page")
def test_edit_name(browser, user_data):
    pofile_page = ProfilePage(browser)
    pofile_page.send_name_in_name_input(user_data['first_name'])
    pofile_page.click_save_changes_button()
    pofile_page.check_success_edit_profile_message_visibility()
