import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []

        # Create UI Elements
        self.task_listbox = tk.Listbox(root, height=10, width=50)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=5)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(side=tk.LEFT, padx=5)

        self.view_button = tk.Button(root, text="View Tasks", command=self.view_tasks)
        self.view_button.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the new task:")
        if task:
            self.tasks.append(task)
            self.view_tasks()

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks.pop(selected_task_index[0])
            messagebox.showinfo("Remove Task", f"Task '{task}' removed.")
            self.view_tasks()
        else:
            messagebox.showwarning("Remove Task", "No task selected.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = simpledialog.askstring("Update Task", "Enter the updated task:")
            if new_task:
                self.tasks[selected_task_index[0]] = new_task
                self.view_tasks()
        else:
            messagebox.showwarning("Update Task", "No task selected.")

    def view_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

# To run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListGUI(root)
    root.mainloop()

