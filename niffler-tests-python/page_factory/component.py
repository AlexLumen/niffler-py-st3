from abc import ABC, abstractmethod

import allure
from playwright.sync_api import expect


class Component(ABC):
    STRATEGIES = {
        "text": lambda page, loc, kw: page.get_by_text(loc, **kw),
        "role": lambda page, loc_dict, kw: page.get_by_role(**loc_dict, **kw),
        "label": lambda page, loc, kw: page.get_by_label(loc, **kw),
        "placeholder": lambda page, loc, kw: page.get_by_placeholder(loc, **kw),
        "alt": lambda page, loc, kw: page.get_by_alt_text(loc, **kw),
        "title": lambda page, loc, kw: page.get_by_title(loc, **kw),
        "css": lambda page, loc, kw: page.locator(loc.format(**kw)),
    }

    def __init__(self, page, locator, name, strategy="css"):
        self.page = page
        self.name = name
        self.locator = locator
        self.strategy = strategy

    @property
    @abstractmethod
    def type_of(self):
        return 'component'

    def get_locator(self, **kwargs):
        strategy_func = self.STRATEGIES.get(self.strategy)
        filtered_kwargs = {k: v for k, v in kwargs.items() if k in ["exact", "timeout", "has_text"]}

        if self.strategy == "role":
            return strategy_func(self.page, self.locator, filtered_kwargs)
        else:
            return strategy_func(self.page, self.locator, kwargs)

    def click(self, **kwargs):
        try:
            with allure.step(f'Нажать {self.type_of}  "{self.name}"'):
                locator = self.get_locator(**kwargs)
                locator.click()
        except Exception:
            allure.attach(
                name="screen",
                body=self.page.screenshot(),
                attachment_type=allure.attachment_type.PNG
            )
            raise Exception(f'Не удалось нажать {self.type_of}  "{self.name}"')

    def click_last(self, **kwargs):
        try:
            with allure.step(f'Нажать на последний {self.type_of} с названием "{self.name}"'):
                locator = self.get_locator(**kwargs)
                locator.last.click()
        except Exception:
            allure.attach(
                name="screen",
                body=self.page.screenshot(),
                attachment_type=allure.attachment_type.PNG
            )
            raise Exception(f'Не удалось нажать на последний {self.type_of}  "{self.name}"')

    def click_first(self, **kwargs):
        try:
            with allure.step(f'Нажать на первый {self.type_of} с названием "{self.name}"'):
                locator = self.get_locator(**kwargs)
                locator.first.click()
        except Exception:
            allure.attach(
                name="screen",
                body=self.page.screenshot(),
                attachment_type=allure.attachment_type.PNG
            )
            raise Exception(f'Не удалось нажать на первый {self.type_of}  "{self.name}"')

    def should_be_visible(self, **kwargs):
        try:
            with allure.step(f'Проверить что {self.type_of} "{self.name}" отображается'):
                locator = self.get_locator(**kwargs)
                expect(locator).to_be_visible()
        except Exception:
            allure.attach(
                name="screen",
                body=self.page.screenshot(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f'{self.type_of} "{self.name}" не отображается')

    def should_not_be_visible(self, **kwargs):
        try:
            with allure.step(f'Проверить что {self.type_of} "{self.name}" не отображается'):
                locator = self.get_locator(**kwargs)
                expect(locator).not_to_be_visible()
        except Exception:
            allure.attach(
                name="screen",
                body=self.page.screenshot(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f'{self.type_of} "{self.name}" отображается')

    def should_have_text(self, text, **kwargs):
        try:
            with allure.step(f'Проверить что {self.type_of} "{self.name}" содержит текст "{text}"'):
                locator = self.get_locator(**kwargs)
                expect(locator).to_have_text(text)
        except Exception:
            allure.attach(
                name="screen",
                body=self.page.screenshot(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f'{self.type_of} "{self.name}" не содержит текст "{text}"')

    def should_have_text_first(self, text, **kwargs):
        try:
            with allure.step(f'Проверить что первый {self.type_of} "{self.name}" содержит текст "{text}"'):
                locator = self.get_locator(**kwargs)
                first_locator = locator.first
                expect(first_locator).to_have_text(text)
        except Exception:
            allure.attach(
                name="screen",
                body=self.page.screenshot(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f'Первый {self.type_of} "{self.name}" не содержит текст "{text}"')

    def get_element_attribute_from_list_by_text(self, text, attribute_name, **kwargs):
        """
         Вернуть атрибут элемента
        """
        try:
            with allure.step(f'Получить атрибут "{attribute_name}" у элемента с текстом "{text}"'):
                locator = self.get_locator(**kwargs)
                locators = locator.all()

                for loc in locators:

                    element_text = loc.text_content().strip()

                    if element_text == text:
                        return loc.get_attribute(attribute_name)
        except Exception:
            allure.attach(
                name="screen",
                body=self.page.screenshot(),
                attachment_type=allure.attachment_type.PNG
            )
            raise Exception(f'Не удалось получить атрибут "{attribute_name}" у элемента с текстом "{text}"')