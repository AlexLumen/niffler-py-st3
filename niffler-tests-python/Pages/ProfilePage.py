from playwright.sync_api import expect

from pages.BasePage import BasePage


class ProfilePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

        self.add_category_input = browser[1].locator("[id='category']")
        self.category_tag = browser[1].locator("[class*='css-14vsv3w']")
        self.category_input_error_message = browser[1].get_by_text("Allowed category length is from 2 to 50 symbols")
        self.edit_category_button = browser[1].locator("[aria-label='Edit category']")
        self.edit_category_input = browser[1].get_by_placeholder("Edit category")
        self.archive_category_button = browser[1].locator("[aria-label='Archive category']")
        self.name_field = browser[1].locator("[id='name']")
        self.save_changes_button = browser[1].locator("[type='submit']")
        self.profile_success_edit_message = browser[1].get_by_text("Profile successfully updated")

    def send_category_name(self, category_value):
        self.add_category_input.fill(category_value)

    def press_enter_in_category_name(self):
        self.add_category_input.focus()
        self.add_category_input.press('Enter')

    def check_added_new_category(self, category_value):
        expect(self.category_tag.first).to_have_text(category_value)

    def check_category_input_error_message(self):
        expect(self.category_input_error_message).to_be_visible()

    def click_edit_category_button(self):
        self.edit_category_button.first.click()

    def send_category_name_in_edit_input(self, category_value):
        self.edit_category_input.fill(f"{category_value}_edited")

    def press_enter_in_edit_category_name(self):
        self.edit_category_input.focus()
        self.edit_category_input.press('Enter')

    def check_edited_category(self, category_value):
        expect(self.category_tag.first).to_have_text(f"{category_value}_edited")

    def click_archive_category_button(self):
        self.archive_category_button.first.click()

    def check_archived_category_not_visibility(self):
        expect(self.category_tag).not_to_be_visible()

    def send_name_in_name_input(self, name):
        self.name_field.fill(name)

    def click_save_changes_button(self):
        self.save_changes_button.click()

    def check_success_edit_profile_message_visibility(self):
        expect(self.profile_success_edit_message).to_be_visible()
