import tkinter as tk
from views.gui.main_window import CRMApp
from utils.database import initialize_db

def main():
    root = tk.Tk()
    app = CRMApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
