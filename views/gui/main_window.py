import tkinter as tk
from tkinter import messagebox
from controllers.customer_controller import CustomerController
from controllers.product_controller import ProductController
from controllers.order_controller import OrderController

class CRMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CRM")

        # Controllers
        self.customer_controller = CustomerController()
        self.product_controller = ProductController()
        self.order_controller = OrderController()

        # GUI Components
        self.label = tk.Label(root, text="Welcome to PyCRM", font=("Helvetica", 16))
        self.label.pack(pady=10)

        # Buttons
        self.button_customer = tk.Button(root, text="Add Customer", command=self.add_customer)
        self.button_customer.pack(pady=5)

        self.button_product = tk.Button(root, text="Add Product", command=self.add_product)
        self.button_product.pack(pady=5)

        self.button_order = tk.Button(root, text="Place Order", command=self.place_order)
        self.button_order.pack(pady=5)

    def add_customer(self):
        # Exemplo: Adicionar cliente
        name = tk.simpledialog.askstring("Add Customer", "Enter customer name:")
        email = tk.simpledialog.askstring("Add Customer", "Enter customer email:")
        phone = tk.simpledialog.askstring("Add Customer", "Enter customer phone:")

        if name and email and phone:
            self.customer_controller.add_customer(name, email, phone)
            messagebox.showinfo("Success", "Customer added successfully!")
        else:
            messagebox.showwarning("Warning", "Please fill in all fields.")

    def add_product(self):
        # Exemplo: Adicionar produto
        name = tk.simpledialog.askstring("Add Product", "Enter product name:")
        price = tk.simpledialog.askfloat("Add Product", "Enter product price:")
        description = tk.simpledialog.askstring("Add Product", "Enter product description:")

        if name and price and description:
            self.product_controller.add_product(name, price, description)
            messagebox.showinfo("Success", "Product added successfully!")
        else:
            messagebox.showwarning("Warning", "Please fill in all fields.")

    def place_order(self):
        # Exemplo: Realizar pedido
        customer_name = tk.simpledialog.askstring("Place Order", "Enter customer name:")
        products = tk.simpledialog.askstring("Place Order", "Enter products (comma-separated):").split(",")

        customer = self.customer_controller.find_customer_by_name(customer_name)
        if not customer:
            messagebox.showwarning("Warning", f"Customer '{customer_name}' not found.")
            return
        
        selected_products = []
        for product_name in products:
            product = self.product_controller.find_product_by_name(product_name.strip())
            if product:
                selected_products.append(product)
            else:
                messagebox.showwarning("Warning", f"Product '{product_name}' not found.")
                return

        if selected_products:
            self.order_controller.create_order(customer, selected_products)
            messagebox.showinfo("Success", "Order placed successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CRMApp(root)
    root.mainloop()
