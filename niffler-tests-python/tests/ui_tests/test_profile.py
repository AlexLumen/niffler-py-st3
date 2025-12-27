import pytest
import allure


@allure.feature("Страница Профиль")
@allure.title("Добавить новую категорию")
@pytest.mark.usefixtures("open_profile_page", "archive_category")
def test_add_new_category(page, category_value, profile_page):
    profile_page.send_category_name(category_value)
    profile_page.press_enter_in_category_name()
    profile_page.check_added_new_category(category_value)


@allure.feature("Страница Профиль")
@allure.title("Отображение сообщения при попытке создать категорию без названия")
@pytest.mark.usefixtures("open_profile_page")
def test_category_input_error_message_if_try_add_category_without_name(page, profile_page):
    profile_page.press_enter_in_category_name()
    profile_page.check_category_input_error_message()


@allure.feature("Страница Профиль")
@allure.title("Редактирование категории")
@pytest.mark.usefixtures("login_user", "archive_category")
def test_edit_category(create_category, navbar_element, profile_page, header_element, page):
    header_element.click_person_icon()
    navbar_element.click_profile_link()
    profile_page.click_edit_category_button()
    profile_page.send_category_name_in_edit_input(create_category.name)
    profile_page.press_enter_in_edit_category_name()
    profile_page.check_edited_category(create_category.name)


@allure.feature("Страница Профиль")
@allure.title("Редактирование категории")
@pytest.mark.usefixtures("login_user", "create_category")
def test_archive_category(page, profile_page, navbar_element, archive_category_alert, header_element):
    header_element.click_person_icon()
    navbar_element.click_profile_link()
    profile_page.click_archive_category_button()
    archive_category_alert.click_archive_button()
    profile_page.check_archived_category_not_visibility()


@allure.feature("Страница Профиль")
@allure.title("Редактирование категории")
@pytest.mark.usefixtures("open_profile_page")
def test_edit_name(page, user_data, profile_page):
    profile_page.send_name_in_name_input(user_data.first_name)
    profile_page.click_save_changes_button()
    profile_page.check_success_edit_profile_message_visibility()
