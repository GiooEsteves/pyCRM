# controllers/customer_controller.py
from models.customer import Customer

class CustomerController:
    def __init__(self):
        self.customers = []

    def add_customer(self, name, email, phone):
        customer = Customer(name, email, phone)
        self.customers.append(customer)

    def list_customers(self):
        return self.customers
