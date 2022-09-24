from base_class import Base


class Shop(Base):
    def __init__(self):
        super().__init__()
        self._capacity: int = 20
        self.__max_unique_items: int = 5

    @property
    def unique_items(self):
        return self._unique_items

    @unique_items.setter
    def unique_items(self, value):
        if value > self.__max_unique_items:
            raise ValueError(f'Shop cannot contain more than {self.__max_unique_items} items')
        self._unique_items = value
