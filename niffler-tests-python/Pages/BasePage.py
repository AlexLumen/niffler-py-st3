
import allure
from playwright.sync_api import Page, expect



class BasePage:
    def __init__(self, page: Page):
        self.browser = page

    def is_element_present(self, locator):
        try:
            expect(locator).to_be_visible()
        except AssertionError:
            return False
        return True

    def open_url(self, url):
        self.browser.goto(url)


    def get_element_attribute_from_list_by_text(self, locator, text, attribute_name):
        """
         Вернуть атрибут элемента
        """
        elements = locator

        count = elements.count()

        for i in range(count):
            element = elements.nth(i)
            element_text = element.text_content().strip()

            if element_text == text:
                return element.get_attribute(attribute_name)

    def assertion_value_exist_in_list(self, locator, expected_value):
        self.browser.wait_for_load_state("domcontentloaded")
        filtered = locator.filter(has_text=expected_value)
        expect(filtered).to_be_visible()



    def chose_element_in_list_by_text(self, locator, text):
        elements = locator
        count = elements.count()

        for i in range(count):
            element = elements.nth(i)
            element_text = element.text_content().strip()
            if element_text == text:
                element.click()
