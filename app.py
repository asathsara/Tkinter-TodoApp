import tkinter as tk
from tkinter import messagebox

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
        self.input_entry.pack(side="left", fill="x", padx=10, pady=10, expand=True)

        self.submit_button = tk.Button(self.second_frame, text="Add", font=("Poppins", 10, "bold"), bg="#339fff",
                                       fg="white", command=self.add_task)
        self.submit_button.pack(side="right", padx=10, pady=10)

        # Frame to hold the list of tasks
        self.task_list_frame = tk.Frame(self.container)
        self.task_list_frame.pack(fill="both", expand=True, pady=10)

        # Load saved tasks into the UI
        self.display_tasks()

    def load_tasks(self):
        try:
            with open("task.txt", "r") as file:
                self.tasks = [line.strip().split(" | ") for line in file]  # Python list comprehension
                self.tasks = [(task[0], task[1] == "True") for task in self.tasks]
        except FileNotFoundError:
            self.tasks = []

    def add_task(self):
        task_text = self.input_entry.get().strip()
        if task_text:
            self.tasks.append((task_text, False))
            self.input_entry.delete(0, tk.END)
            self.display_tasks()
            self.save_tasks()

    def save_tasks(self):
        with open("task.txt", "w") as file:
            for task, completed in self.tasks:
                file.write(f"{task} | {completed}\n")

    def display_tasks(self):
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()

        for task, completed in self.tasks:
            self.create_task_item(task, completed)

    def create_task_item(self, task_text, completed):
        task_frame = tk.Frame(self.task_list_frame, pady=2)
        task_frame.pack(fill="x", padx=5, pady=2)

        task_label = tk.Label(task_frame, text=task_text, font=("Poppins", 12, "overstrike" if completed else ""),
                              anchor="w", cursor="hand2")
        task_label.pack(side="left", fill="x", expand=True, padx=5)

        # Bind left mouse click (Button-1) to the label
        task_label.bind("<Button-1>", lambda event, task=task_text, frame=task_frame: self.toggle_task(task, frame))

        delete_button = tk.Button(
            task_frame, text="❌", font=("Poppins", 10),
            command=lambda: self.confirm_delete(task_text, task_frame)
        )
        delete_button.pack(side="right", padx=5)

    def delete_task(self, task_text, task_frame):
        task_frame.destroy()
        # Remove the entire tuple from self.tasks
        self.tasks = [task for task in self.tasks if task[0] != task_text]
        self.save_tasks()

    def toggle_task(self, task_text, task_frame):
        for widget in task_frame.winfo_children():
            if isinstance(widget, tk.Label):
                current_font = widget.cget("font")
                if "overstrike" in current_font:
                    widget.config(font=("Poppins", 12))  # Remove strikethrough
                    self.update_task_status(task_text, False)  # Mark as not completed
                else:
                    widget.config(font=("Poppins", 12, "overstrike"))  # Apply strikethrough
                    self.update_task_status(task_text, True)  # Mark as completed

    def update_task_status(self, task_text, completed):
        for idx, (task, status) in enumerate(self.tasks):
            if task == task_text:
                self.tasks[idx] = (task_text, completed)  # Update task status
                self.save_tasks()
                break

    def confirm_delete(self, task_text, task_frame):
        res = messagebox.askquestion("Delete", f"Do you really want to delete {task_text}?")

        if res == "yes":
            self.delete_task(task_text, task_frame)


# Create the main window
main_window = tk.Tk()

# Initialize the app
app = TodoApp(main_window)

# Start the GUI loop
main_window.mainloop()
