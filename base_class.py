from storage_class import Storage


class Base(Storage):
    def __init__(self):
        self._items: dict = {}
        self._capacity: int = 0
        self._unique_items: int = 0

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    @property
    def unique_items(self):
        return self._unique_items

    @unique_items.setter
    def unique_items(self, value):
        self._unique_items = value

    def add(self, item_name: str, item_amount: int):
        if self.capacity == 0:
            raise ValueError('Storage is already full')

        if item_name not in self.items.keys():
            self._items.update({item_name: item_amount})
            self.unique_items = len(self.items.keys())
        else:
            self.items[item_name] += item_amount

        self._capacity -= item_amount

    def remove(self, item_name: str, item_amount: int):
        if item_name not in self.items.keys():
            raise ValueError('No such item in the storage')

        if item_amount > self.items[item_name]:
            raise ValueError('No such amount of item in the storage')

        self.items[item_name] -= item_amount

        if self.items[item_name] == 0:
            del self.items[item_name]
            self.unique_items = len(self.items.keys())
            self._capacity += item_amount

    def get_items(self):
        return "\n".join([f'{k}: {v}' for k, v in self.items.items()])

    def get_free_space(self):
        return self.capacity

    def get_unique_items_count(self):
        return self.unique_items