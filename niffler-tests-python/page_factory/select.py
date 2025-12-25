from page_factory.component import Component
import allure


class Select(Component):
    @property
    def type_of(self):
        return 'select'

    def chose_element_in_list_by_text(self, text, **kwargs):
        with allure.step(f'Выбрать из списка {self.type_of} с названием "{self.name}" по тексту {text}'):
            locator = self.get_locator(**kwargs)
            elements = locator
            count = elements.count()

            for i in range(count):
                element = elements.nth(i)
                element_text = element.text_content().strip()
                if element_text == text:
                    element.click()
