

from page_factory.component import Component


class Form(Component):
    @property
    def type_of(self):
        return 'form'
