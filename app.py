import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x600")


# Create the main window
root = tk.Tk()
app = TodoApp(root)

# Start the GUI loop
root.mainloop()
