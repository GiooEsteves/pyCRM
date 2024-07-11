from utils.database import get_db_connection

class CustomerController:
    def __init__(self):
        self.conn = get_db_connection()
        
    def add_customer(self, name, email, phone):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        self.conn.commit()
        cursor.close()

    def find_customer_by_name(self, name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE name=%s", (name,))
        result = cursor.fetchone()
        cursor.close()
        return result
