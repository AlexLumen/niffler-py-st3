import allure
from playwright.sync_api import expect

from page_factory.component import Component


class Input(Component):
    @property
    def type_of(self):
        return 'input'

    def fill(self, value, **kwargs):
        try:
            with allure.step(f'Ввести в {self.type_of} "{self.name}" значение "{value}"'):
                locator = self.get_locator(**kwargs)
                locator.fill(value)
        except Exception:
            allure.attach(
                name="screen",
                body=self.page.screenshot(),
                attachment_type=allure.attachment_type.PNG
            )
            raise Exception(f'Не удалось ввести в {self.type_of} "{self.name}" значение "{value}"')

    def focus(self, **kwargs):
        try:
            with allure.step(f'Навести курсор на {self.type_of} "{self.name}"'):
                locator = self.get_locator(**kwargs)
                locator.focus()
        except Exception:
            allure.attach(
                name="screen",
                body=self.page.screenshot(),
                attachment_type=allure.attachment_type.PNG
            )
            raise Exception(f'Не удалось навести курсор на {self.type_of} "{self.name}"')

    def press(self, key, **kwargs):
        try:
            with allure.step(f'Нажать на клавиатуре на элементе {self.type_of} "{self.name}" '):
                locator = self.get_locator(**kwargs)
                locator.press(key)
        except Exception:
            allure.attach(
                name="screen",
                body=self.page.screenshot(),
                attachment_type=allure.attachment_type.PNG
            )
            raise KeyboardInterrupt(f'Не удалось нажать на клавиатуре на элементе {self.type_of} "{self.name}"')

