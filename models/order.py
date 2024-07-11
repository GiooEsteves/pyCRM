# models/order.py
class Order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products
        self.total = sum(product.price for product in products)

    def __str__(self):
        product_list = "\n".join(f"{product.name}: ${product.price}" for product in self.products)
        return f"Customer: {self.customer.name}\nProducts:\n{product_list}\nTotal: ${self.total}"
