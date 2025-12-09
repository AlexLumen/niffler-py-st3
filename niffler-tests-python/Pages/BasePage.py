import logging
import allure


from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.logger = logging.getLogger(type(self).__name__)

    def verify_element_visibility(self, how, what, timeout=10):
        """
        Проверить присутствие элемента
        """
        try:
            self.logger.info(f"Wait {what} to be visibility")
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            self.logger.error(f"Element {what} is not visibility in page")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError("Не дождался видимости элемента: {}".format(what))

    def click_element(self, how, what):
        """Кликнуть по элементу"""
        try:
            self.logger.info(f"Wait {what} to be visibility")
            self.verify_element_visibility(how, what)
            element = self.browser.find_element(how, what)
            element.click()
        except NoSuchElementException:
            self.logger.error(f"Element '{what}' not found on page!")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Element '{what}' not found on page!")

    def get_text(self, how, what):
        """Получить текст элемента"""
        try:

            self.logger.info("Get text: {}".format(what))
            self.verify_element_visibility(how, what)
            element_text = self.browser.find_element(how, what).text
            return element_text
        except NoSuchElementException:
            self.logger.error(f"Element '{what}' not found on page!")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Element '{what}' not found on page!")

    def send_text(self, how, what, text):
        """Напечатать текст"""
        try:
            self.verify_element_visibility(how, what)
            element = self.browser.find_element(how, what)
            self.logger.info("Clearing text: {}".format(what))
            element.clear()
            self.logger.info("Input text: {}".format(what))
            element.send_keys(text)
        except NoSuchElementException:
            self.logger.error(f"Element '{what}' not found on page!")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Element '{what}' not found on page!")

    def assertion(self, element_text, expected_text):
        """Сравнение ожидаемого и фактического результата"""
        try:
            assert element_text == expected_text
        except Exception:
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Результат: {element_text}, Ожидалось: {expected_text}")
