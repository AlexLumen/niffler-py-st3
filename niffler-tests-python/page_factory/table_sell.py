import time

from playwright.async_api import expect

from page_factory.component import Component
import allure


class TableSell(Component):
    @property
    def type_of(self):
        return 'table sell'

    def assertion_value_exist_in_list(self, expected_value, **kwargs):
        try:
            with allure.step(f'Проверить что  в списке{self.type_of} с названием "{self.name}" есть {expected_value}'):
                self.page.wait_for_load_state("load")
                locator = self.get_locator(**kwargs)
                locator.wait_for(state="visible", timeout=5000)

                locators = locator.all()
                value_list = []
                for loc in locators:
                    value_list.append(loc.inner_text())

                assert expected_value in value_list
        except Exception:
            allure.attach(
                name="screen",
                body=self.page.screenshot(),
                attachment_type=allure.attachment_type.PNG
            )
            raise KeyboardInterrupt(f'Отсутствует в списке{self.type_of} "{self.name}" есть {expected_value}')
