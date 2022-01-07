class Item:
    def __init__(self, _id, name, price) -> None:
        self._id = _id
        self.name = name
        self.price = price

    @staticmethod
    def json(id, name, price):
        return {'id': id, 'name': name, 'price': price}

    @classmethod
    def constructor(cls, name, price):
        return cls(None, name, price)
