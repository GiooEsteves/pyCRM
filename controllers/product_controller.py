from utils.database import get_db_connection

class ProductController:
    def __init__(self):
        self.conn = get_db_connection()

    def add_product(self, name, price, description):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO products (name, price, description) VALUES (%s, %s, %s)", (name, price, description))
        self.conn.commit()
        cursor.close()

    def find_product_by_name(self, name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products WHERE name=%s", (name,))
        result = cursor.fetchone()
        cursor.close()
        return result
