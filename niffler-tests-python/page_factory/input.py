import allure
from playwright.sync_api import expect

from page_factory.component import Component


class Input(Component):
    @property
    def type_of(self):
        return 'input'

    def fill(self, value, **kwargs):
        with allure.step(f'ввести {self.type_of} "{self.name}" значение "{value}"'):
            locator = self.get_locator(**kwargs)
            locator.fill(value)

    def focus(self, **kwargs):
        with allure.step(f'Навести курсов на {self.type_of} "{self.name}" '):
            locator = self.get_locator(**kwargs)
            locator.focus()

    def press(self, key, **kwargs):
        with allure.step(f'Нажать на клавиатуре на элементе {self.type_of} "{self.name}" '):
            locator = self.get_locator(**kwargs)
            locator.press(key)
