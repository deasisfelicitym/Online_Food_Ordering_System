class Cart:
    def __init__(self, product, register):
        self.product = product
        self.register = register

    def view_cart(self):

        username = input("Enter Username: ")

        if username not in self.product.orders:
            print("No orders found!")
            return

        print("\n==================== ORDER DETAILS ====================\n")

        print(f"{'Order':20} {'Quantity':10} {'Price':10} {'Total':10}")
        print("------------------------------------------------------------")

        total_payment = 0

        for item in self.product.orders[username]:
            total = item.get_total()
            total_payment += total


            print(
                f"{item.food:20} "
                f"{item.quantity:<10} "
                f"{item.price:<10.2f} "
                f"{total:<10.2f}"
            # < for left alignment
            )

        print("------------------------------------------------------------")
        print(f"\nTotal Payment     : {total_payment:.2f}")
