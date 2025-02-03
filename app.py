import tkinter as tk
from PIL import Image, ImageTk  # Import PIL for image processing

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x600")
        self.root.title("Todo App")

        self.tasks = []
        self.load_tasks()

        # Container frame
        self.container = tk.Frame(root, padx=8, pady=8)  # margin
        self.container.pack(fill="both", expand=True)

        # Frame for the image and text label to be on the same line
        self.top_frame = tk.Frame(self.container)
        self.top_frame.pack(side="top", fill="x")

        self.second_frame = tk.Frame(self.container)
        self.second_frame.pack(side="top", fill="x")

        # Open and resize the image
        image = Image.open("assets/calendar.png")
        image = image.resize((26, 26))

        # Convert to Tkinter-compatible format
        self.photo = ImageTk.PhotoImage(image)

        # Image label
        self.image_label = tk.Label(self.top_frame, image=self.photo)
        self.image_label.pack(side="left", padx=10)

        # Text label next to the image
        self.text_label = tk.Label(self.top_frame, text="Task List", font=("Poppins", 16, "bold"))
        self.text_label.pack(side="left", pady=10)

        # Input field (in a new line below)
        self.input_entry = tk.Entry(self.second_frame, bd=1, font=("Poppins", 12))
        self.input_entry.pack(side="left", fill="x", padx=10, pady=10,expand=True)

        self.submit_button = tk.Button(self.second_frame, text="Add", font=("Poppins", 10, "bold"), bg="#339fff", fg="white")
        self.submit_button.pack(side="right", padx=10, pady=10)

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
