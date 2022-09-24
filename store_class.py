from base_class import Base


class Store(Base):
    def __init__(self):
        super().__init__()
        self._capacity: int = 100
