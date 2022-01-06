class Item:
    def __init__(self, _id, name, price) -> None:
        self._id = _id
        self.name = name
        self.price = price

    def json(self):
        return {'id': self._id, 'name': self.name, 'price': self.price}
