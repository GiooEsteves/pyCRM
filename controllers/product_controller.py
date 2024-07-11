# controllers/product_controller.py
from models.product import Product

class ProductController:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, description):
        product = Product(name, price, description)
        self.products.append(product)

    def list_products(self):
        return self.products
