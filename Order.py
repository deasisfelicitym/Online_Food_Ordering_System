class Order:
    def __init__(self, food, quantity, price):
        self.food = food
        self.quantity = quantity
        self.price = price

    def get_total(self):
        return self.quantity * self.price

# order class is used to encapsulate order information. Instead of using dictionaries,
# each food order is stored as an order object.
# This contains get_total method to calculate the total price