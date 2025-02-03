import tkinter as tk
from PIL import Image, ImageTk  # Import PIL for image processing

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x600")

        self.tasks = []
        self.load_tasks()

        self.container = tk.Frame(root, padx=8, pady=8) # margin
        self.container.grid(row=0, column=0, sticky="nsew")

        # Open and resize the image
        image = Image.open("assets/calendar.png")
        image = image.resize((26, 26))  # Set the desired size

        # Convert to Tkinter-compatible format
        self.photo = ImageTk.PhotoImage(image)

        self.image_label = tk.Label(self.container, image=self.photo)
        self.image_label.grid(row=0, column=0, padx=10, pady=10)

        # Create text label next to the image
        self.text_label = tk.Label(self.container, text="Task List", font=("Poppins", 16,"bold"))
        self.text_label.grid(row=0, column=1, pady=10)

    def load_tasks(self):
        try:
            with open("task.txt", "r") as file:
                self.tasks = [line.strip() for line in file]  # Python list comprehension
        except FileNotFoundError:
            self.tasks = []

# Create the main window
root = tk.Tk()

# Initialize the app
app = TodoApp(root)

# Start the GUI loop
root.mainloop()
