class Receipt:
    def __init__(self, product, register):
        self.product = product
        self.register = register

    def payment_details(self):

        username = input("Enter Username: ")

        if username not in self.register.customers:
            print("Customer not found!")
            return

        if username not in self.product.orders:
            print("No orders found!")
            return

        customer = self.register.customers[username]

        print("\n===================== TRANSACTION DETAILS =====================\n")

        print(f"Customer Name     : {customer['name']}")
        print(f"Customer Username : {username}")
        print(f"Contact Number    : {customer['contact']}")
        print(f"Address           : {customer['address']}")

        print("\n------------------------------------------------------------")
        print(f"{'Order':20} {'Quantity':10} {'Price':10} {'Total':10}")
        print("------------------------------------------------------------")

        subtotal = 0

        for item in self.product.orders[username]:

            total = item.get_total()
            subtotal += total

            print(
                f"{item.food:20} "
                f"{item.quantity:<10} "
                f"{item.price:<10.2f} "
                f"{total:<10.2f}"
            )

        delivery_fee = 50.00
        grand_total = subtotal + delivery_fee

        try:
            file = open("receipt.txt", "a")

            file.write(
                f"{customer['name']},"
                f"{username},"
                f"{customer['contact']},"
                f"{customer['address']},"
                f"{subtotal:.2f},"
                f"{grand_total:.2f}\n"
            )

            file.close()

        except FileNotFoundError:
            print("Unable to save receipt.")



        print("------------------------------------------------------------")

        print(f"\nSubtotal          : {subtotal:.2f}")
        print(f"Delivery Fee      : {delivery_fee:.2f}")
        print(f"Total Amount      : {grand_total:.2f}")

        print("\nPayment Method    : Cash on Delivery")

        print("\nThank you for ordering!")