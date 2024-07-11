# views/cli.py
from controllers.customer_controller import CustomerController

class CLI:
    def __init__(self):
        self.customer_controller = CustomerController()

    def run(self):
        print("Welcome to CRM CLI")
        while True:
            command = input("Enter command (add_customer, list_customers, exit): ")
            if command == "add_customer":
                name = input("Enter customer name: ")
                email = input("Enter customer email: ")
                phone = input("Enter customer phone: ")
                self.customer_controller.add_customer(name, email, phone)
                print("Customer added successfully!")
            elif command == "list_customers":
                customers = self.customer_controller.list_customers()
                if not customers:
                    print("No customers found.")
                else:
                    print("List of customers:")
                    for customer in customers:
                        print(f"{customer.name} - {customer.email} - {customer.phone}")
            elif command == "exit":
                print("Exiting CRM CLI. Goodbye!")
                break
            else:
                print("Invalid command. Try again.")
