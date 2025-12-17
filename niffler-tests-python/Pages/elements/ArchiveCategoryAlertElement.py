from Pages.BasePage import BasePage


class ArchiveCategoryAlertElement(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.archive_button = browser[1].get_by_text("Archive")

    def click_archive_button(self):
        self.archive_button.last.click()
