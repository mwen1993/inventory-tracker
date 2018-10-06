class Shoe:

    def __init__(self, name, color, size, purchased_price, sold_price=None):
        self.name = name.title()
        self.color = color.title()
        self.size = size
        self.purchased_price = purchased_price
        self.sold_price = sold_price
