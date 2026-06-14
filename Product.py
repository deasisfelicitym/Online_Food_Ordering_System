from Order import Order

class Product:
    def __init__(self, register):
        self.register = register

        self.menu = {
            "A": ("Burger", 65.00),
            "B": ("Fries", 50.00),
            "C": ("Chicken with Rice", 120.00),
            "D": ("Chicken Fillet", 155.00),
            "E": ("Takoyaki", 80.00),
            "F": ("Float", 75.00),
            "G": ("Fruit Soda", 45.00)
        }

        self.orders = {}

        try:
            path = "orders.txt"

            file = open(path, "r")

            for line in file:

                username, food, qty, price = line.strip().split(",")

                if username not in self.orders:
                    self.orders[username] = []

                order = Order(
                    food,
                    int(qty),
                    float(price)
                )

                self.orders[username].append(order)

            file.close()

        except FileNotFoundError:
            print("No order records found.")



    def food_menu(self):

        print("\n==================== MENU ====================")
        print("||========== Please select your order")
        print("     FOODS                  PRICE")

        for code, item in self.menu.items():
            print(f"[{code}] {item[0]:20} : {item[1]:8.2f}")
        # 20 spaces for food name, f = float, 8 spaces, 2 decimals

        username = input("\nEnter Username: ")

        if username.strip() == "":
            print("Username cannot be empty!")
            return

        if username not in self.register.customers:
            print("Customer not found!")
            return

        if username not in self.orders:
            self.orders[username] = []

        while True:

            order_code = input("Enter your order: ").upper()

            if order_code not in self.menu:
                print("Invalid order!")
                continue

            try:
                qty = int(input("Enter Quantity: "))

                if qty <= 0:
                    print("Quantity must be greater than zero.")
                    continue

            except ValueError:
                print("Invalid quantity!")
                continue

            food_name, price = self.menu[order_code]

            order = Order(
                food_name,
                qty,
                price
            )

            self.orders[username].append(order)

            try:
                path = "orders.txt"

                file = open(path, "a")

                file.write(
                    f"{username},{food_name},{qty},{price:2f}\n"
                )

                file.close()

            except FileNotFoundError:
                print("Unable to save order.")

            while True:

                another = input(
                    "Would you like to add another order [Y/N]: "
                ).upper()

                if another == "Y":
                    break

                elif another == "N":
                    print("\nOrder successfully saved!")
                    print("\n---Please proceed to cart to checkout")
                    return

                else:
                    print("Please enter Y or N only.")