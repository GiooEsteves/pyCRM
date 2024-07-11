# controllers/order_controller.py
from models.order import Order

class OrderController:
    def __init__(self):
        self.orders = []

    def create_order(self, customer, products):
        order = Order(customer, products)
        self.orders.append(order)

    def list_orders(self):
        return self.orders
