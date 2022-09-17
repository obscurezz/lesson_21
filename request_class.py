from shop_class import Shop
from store_class import Store


class Request:
    def __init__(self, store: Store, shop: Shop, message: str):
        """
        :selling_objects: dict, where key is name of shop or store in message and value is an exact object
        :param message: format: Deliver <amount> <item> from <store> to <shop>
        """
        self.amount: int = int(message.split()[1])
        self.item: str = message.split()[2]
        self.from_keyword: str = message.split()[4]
        self.to_keyword: str = message.split()[6]

        self.store = store
        self.shop = shop

    def __repr__(self):
        return '\n'.join([f'from = {self.from_keyword}',
                          f'to = {self.to_keyword}',
                          f'amount = {self.amount}',
                          f'item = {self.item}'])
