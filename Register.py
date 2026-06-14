class Register:
    def __init__(self):
        self.customers = {}

        try:
            path = "customers.txt"

            file = open(path, "r")

            for line in file:
                username, name, contact, address = line.strip().split(",")

                self.customers[username] = {
                    "name": name,
                    "contact": contact,
                    "address": address
                }

            file.close()

        except FileNotFoundError:
            print("No customer records found.")


    def customer_registration(self):

        name = input("Enter Customer Name: ")

        username = input("Enter Customer Username: ")

        if not username:
            print("Username is required!")
            return

        if username in self.customers:
            print("Username already exists!")
            return

        contact = input("Enter Contact Number: ")
        address = input("Enter Address: ")

        if not name or not contact or not address:
            print("All fields are required!")
            return

        self.customers[username] = {
            "name": name,
            "contact": contact,
            "address": address
        }

        try:
            path = "customers.txt"

            file = open(path, "a")
            # using append because i want my costumer to have multiple order

            file.write(
                f"{username},{name},{contact},{address}\n"
            )

            file.close()

        except FileNotFoundError:
            print("No customer records found.")


        print("\n================ CUSTOMER DETAILS ================")
        print("Customer Name:", name)
        print("Customer Username:", username)
        print("Contact Number:", contact)
        print("Address:", address)

        print("\nCustomer successfully saved.")