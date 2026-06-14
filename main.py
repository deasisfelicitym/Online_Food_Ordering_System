from Register import Register
from Product import Product
from Cart import Cart
from Receipt import Receipt

register = Register()
product = Product(register)
cart = Cart(product, register)
receipt = Receipt(product, register)

print("Online Food Ordering System")

while True:

    print("\n==================== WELCOME! ====================")
    print("||===== Please select your choice from 1-4")
    print("[1] Customer Registration")
    print("[2] Food Menu")
    print("[3] View Cart to Checkout")
    print("[4] Payment Details")
    print("[0] Exit")

    print("\n---------------------------------------------------")

    choice = input("Enter your choice: ")

    if choice == "1":
        register.customer_registration()

    elif choice == "2":
        product.food_menu()

    elif choice == "3":
        cart.view_cart()

    elif choice == "4":
        receipt.payment_details()

    elif choice == "0":
        print("Thank you for checking out our store!")
        break

    else:
        print("Invalid choice!")