import mysql.connector
from mysql.connector import Error
from utils.logger import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
 
def initialize_db():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            cursor.execute(f"USE {DB_NAME}")
            
            cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                name VARCHAR(255) NOT NULL,
                                email VARCHAR(255) NOT NULL,
                                phone VARCHAR(20) NOT NULL
                              )''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                name VARCHAR(255) NOT NULL,
                                price DECIMAL(10, 2) NOT NULL,
                                description TEXT
                              )''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                customer_id INT NOT NULL,
                                product_ids TEXT NOT NULL,
                                FOREIGN KEY(customer_id) REFERENCES customers(id)
                              )''')
            
            conn.commit()
            cursor.close()
            conn.close()
    except Error as e:
        print(f"Error: '{e}'")

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except Error as e:
        print(f"Error: '{e}'")
        return None
