

from page_factory.component import Component


class Paragraph(Component):
    @property
    def type_of(self):
        return 'text'
