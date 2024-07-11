# views/cli.py
from controllers.customer_controller import CustomerController
from controllers.product_controller import ProductController
from controllers.order_controller import OrderController
from models.product import Product

class CLI:
    def __init__(self):
        self.customer_controller = CustomerController()
        self.product_controller = ProductController()
        self.order_controller = OrderController()

    def run(self):
        print("Welcome to PyCRM CLI")
        while True:
            command = input("Enter command (add_customer, list_customers, add_product, list_products, add_order, list_orders, exit): ")
            if command == "add_customer":
                self.add_customer()
            elif command == "list_customers":
                self.list_customers()
            elif command == "add_product":
                self.add_product()
            elif command == "list_products":
                self.list_products()
            elif command == "add_order":
                self.add_order()
            elif command == "list_orders":
                self.list_orders()
            elif command == "exit":
                print("Exiting PyCRM CLI. Goodbye!")
                break
            else:
                print("Invalid command. Try again.")

    def add_customer(self):
        name = input("Enter customer name: ")
        email = input("Enter customer email: ")
        phone = input("Enter customer phone: ")
        self.customer_controller.add_customer(name, email, phone)
        print("Customer added successfully!")

    def list_customers(self):
        customers = self.customer_controller.list_customers()
        if not customers:
            print("No customers found.")
        else:
            print("List of customers:")
            for customer in customers:
                print(f"{customer.name} - {customer.email} - {customer.phone}")

    def add_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        description = input("Enter product description: ")
        self.product_controller.add_product(name, price, description)
        print("Product added successfully!")

    def list_products(self):
        products = self.product_controller.list_products()
        if not products:
            print("No products found.")
        else:
            print("List of products:")
            for product in products:
                print(f"{product.name} - ${product.price} - {product.description}")

    def add_order(self):
        customers = self.customer_controller.list_customers()
        if not customers:
            print("No customers found. Please add a customer first.")
            return

        print("Select a customer to place the order:")
        for index, customer in enumerate(customers):
            print(f"{index + 1}. {customer.name}")

        try:
            customer_index = int(input("Enter customer number: ")) - 1
            selected_customer = customers[customer_index]
        except (ValueError, IndexError):
            print("Invalid input. Aborting order creation.")
            return

        products = []
        while True:
            products_list = self.product_controller.list_products()
            if not products_list:
                print("No products found. Please add products first.")
                return

            print("Select a product to add to the order (or type 'done' to finish):")
            for index, product in enumerate(products_list):
                print(f"{index + 1}. {product.name} - ${product.price}")

            product_input = input("Enter product number or 'done': ")
            if product_input == "done":
                break

            try:
                product_index = int(product_input) - 1
                selected_product = products_list[product_index]
                products.append(selected_product)
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")

        if products:
            self.order_controller.create_order(selected_customer, products)
            print("Order created successfully!")

    def list_orders(self):
        orders = self.order_controller.list_orders()
        if not orders:
            print("No orders found.")
        else:
            print("List of orders:")
            for order in orders:
                print(order)
                print("---------------")

