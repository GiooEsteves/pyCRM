import tkinter as tk
from tkinter import simpledialog, messagebox
from controllers.customer_controller import CustomerController
from controllers.product_controller import ProductController
from controllers.order_controller import OrderController

class CRMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("crm")
        
        # Definir tamanho da janela
        window_width = 800
        window_height = 600
        
        # Obter tamanho da tela
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        # Calcular posição para centralizar a janela
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        
        # Definir geometria da janela
        root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        # Frame para centralizar o conteúdo
        self.frame = tk.Frame(root)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Controllers
        self.customer_controller = CustomerController()
        self.product_controller = ProductController()
        self.order_controller = OrderController()

        # GUI Components
        self.label = tk.Label(self.frame, text=" CRM ", font=("Helvetica", 16))
        self.label.pack(pady=10)

        # Buttons
        self.button_customer = tk.Button(self.frame, text="Add Customer", command=self.add_customer)
        self.button_customer.pack(pady=5)

        self.button_product = tk.Button(self.frame, text="Add Product", command=self.add_product)
        self.button_product.pack(pady=5)

        self.button_order = tk.Button(self.frame, text="Place Order", command=self.place_order)
        self.button_order.pack(pady=5)

    def add_customer(self):
        name = simpledialog.askstring("Add Customer", "Enter customer name:")
        email = simpledialog.askstring("Add Customer", "Enter customer email:")
        phone = simpledialog.askstring("Add Customer", "Enter customer phone:")

        if name and email and phone:
            self.customer_controller.add_customer(name, email, phone)
            messagebox.showinfo("Success", "Customer added successfully!")
        else:
            messagebox.showwarning("Warning", "Please fill in all fields.")

    def add_product(self):
        name = simpledialog.askstring("Add Product", "Enter product name:")
        price = simpledialog.askfloat("Add Product", "Enter product price:")
        description = simpledialog.askstring("Add Product", "Enter product description:")

        if name and price and description:
            self.product_controller.add_product(name, price, description)
            messagebox.showinfo("Success", "Product added successfully!")
        else:
            messagebox.showwarning("Warning", "Please fill in all fields.")

    def place_order(self):
        customer_name = simpledialog.askstring("Place Order", "Enter customer name:")
        products = simpledialog.askstring("Place Order", "Enter products (comma-separated):").split(",")

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
