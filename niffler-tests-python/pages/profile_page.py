

from page_factory.button import Button
from page_factory.input import Input
from page_factory.paragraph import Paragraph
from page_factory.tag import Tag



class ProfilePage:
    def __init__(self, page):

        self.add_category_input = Input(page, locator="[id='category']", name="Add category")
        self.category_tag = Tag(page, locator="[class*='css-14vsv3w']", name="Category tag")
        self.category_input_error_message = Paragraph(page, locator="Allowed category length is from "
                                                                                     "2 to 50 symbols",
                                                      name="Invalid lenght message", strategy="text")
        self.edit_category_button = Button(page, locator="[aria-label='Edit category']", name="Edit category")
        self.edit_category_input = Input(page, locator="Edit category", name="Edit category", strategy="placeholder")
        self.archive_category_button = Button(page, locator="[aria-label='Archive category']", name="Archive button")
        self.name_field = Input(page, locator="[id='name']", name="Name")
        self.save_changes_button = Button(page, locator="[type='submit']", name="Save")
        self.profile_success_edit_message = Paragraph(page, locator="Profile successfully updated",
                                                      name="Success edit message", strategy="text")

    def send_category_name(self, category_value):
        self.add_category_input.fill(category_value)

    def press_enter_in_category_name(self):
        self.add_category_input.focus()
        self.add_category_input.press('Enter')

    def check_added_new_category(self, category_value):
        self.category_tag.should_have_text_first(category_value)

    def check_category_input_error_message(self):
        self.category_input_error_message.should_be_visible()

    def click_edit_category_button(self):
        self.edit_category_button.click_first()

    def send_category_name_in_edit_input(self, category_value):
        self.edit_category_input.fill(f"{category_value}_edited")

    def press_enter_in_edit_category_name(self):
        self.edit_category_input.focus()
        self.edit_category_input.press('Enter')

    def check_edited_category(self, category_value):
        self.category_tag.should_have_text_first(f"{category_value}_edited")

    def click_archive_category_button(self):
        self.archive_category_button.click_first()

    def check_archived_category_not_visibility(self):
        self.category_tag.should_not_be_visible()

    def send_name_in_name_input(self, name):
        self.name_field.fill(name)

    def click_save_changes_button(self):
        self.save_changes_button.click()

    def check_success_edit_profile_message_visibility(self):
        self.profile_success_edit_message.should_be_visible()
