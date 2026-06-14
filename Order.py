class Order:
    def __init__(self, food, quantity, price):
        self.food = food
        self.quantity = quantity
        self.price = price

    def get_total(self):
        return self.quantity * self.price