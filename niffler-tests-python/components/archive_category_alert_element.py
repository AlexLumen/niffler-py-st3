from page_factory.button import Button


class ArchiveCategoryAlertElement:
    def __init__(self, page):
        self.archive_button = Button(page, locator=".MuiDialogActions-root>.MuiButtonBase-root:nth-child(2)",
                                     name="Archive")

    def click_archive_button(self):
        self.archive_button.click_last()
