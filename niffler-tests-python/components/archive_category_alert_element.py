from page_factory.button import Button


class ArchiveCategoryAlertElement:
    def __init__(self, page):
        self.archive_button = Button(page, locator="Archive", name="Archive", strategy="text")

    def click_archive_button(self):
        self.archive_button.click_last()
