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

        if self.strategy == "role":
            filtered_kwargs = {k: v for k, v in kwargs.items() if k in ["exact", "timeout", "has_text"]}
            return strategy_func(self.page, self.locator, filtered_kwargs)
        return strategy_func(self.page, self.locator, kwargs)

    def click(self, **kwargs):
        with allure.step(f'Нажать {self.type_of}  "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.click()

    def click_last(self, **kwargs):
        with allure.step(f'Нажать на последний {self.type_of} с названием "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.last.click()

    def click_first(self, **kwargs):
        with allure.step(f'Нажать на первый {self.type_of} с названием "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.first.click()

    def should_be_visible(self, **kwargs):
        with allure.step(f'Проверить что {self.type_of} "{self.name}" отображается'):
            locator = self.get_locator(**kwargs)
            expect(locator).to_be_visible()

    def should_not_be_visible(self, **kwargs):
        with allure.step(f'Проверить что {self.type_of} "{self.name}" не отображается'):
            locator = self.get_locator(**kwargs)
            expect(locator).not_to_be_visible()

    def should_not_be_visible_by_text(self, text, **kwargs):
        with allure.step(f'Проверить что {self.type_of} "{self.name}" не отображается'):
            locator = self.get_locator(**kwargs).filter(has_text=text)
            expect(locator).not_to_be_visible()

    def should_have_text(self, text, **kwargs):
        with allure.step(f'Проверить что {self.type_of} "{self.name}" содержит текст "{text}"'):
            locator = self.get_locator(**kwargs)
            expect(locator).to_have_text(text)

    def should_have_text_filtered(self, text, **kwargs):
        with allure.step(f'Проверить что {self.type_of} "{self.name}" содержит текст "{text}"'):
            locator = self.get_locator(**kwargs)
            first_locator = locator.filter(has_text=text)
            expect(first_locator).to_have_text(text)

    def get_element_attribute_from_list_by_text(self, text, attribute_name, **kwargs):
        """
         Вернуть атрибут элемента
        """
        with allure.step(f'Получить атрибут "{attribute_name}" у элемента с текстом "{text}"'):
            locator = self.get_locator(**kwargs)
            locators = locator.all()

            for loc in locators:

                element_text = loc.text_content().strip()

                if element_text == text:
                    return loc.get_attribute(attribute_name)
