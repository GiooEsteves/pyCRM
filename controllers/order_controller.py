from utils.database import get_db_connection

class OrderController:
    def __init__(self):
        self.conn = get_db_connection()

    def create_order(self, customer, products):
        cursor = self.conn.cursor()
        product_ids = ",".join([str(product[0]) for product in products])
        cursor.execute("INSERT INTO orders (customer_id, product_ids) VALUES (%s, %s)", (customer[0], product_ids))
        self.conn.commit()
        cursor.close()
