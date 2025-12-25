from page_factory.component import Component


class Tag(Component):
    @property
    def type_of(self):
        return 'tag'

