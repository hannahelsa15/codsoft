import tkinter as tk
from tkinter import messagebox
import json

# File to store tasks
FILE_PATH = 'tasks_gui.json'

# Load tasks from file or initialize an empty list if file doesn't exist
def load_tasks():
    try:
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to the file
def save_tasks(tasks):
    with open(FILE_PATH, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add task to the list
def add_task():
    task = entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks(tasks)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Mark task as completed
def complete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["completed"] = True
        listbox.delete(index)
        listbox.insert(index, f"{tasks[index]['task']} - [Completed]")
        save_tasks(tasks)
    else:
        messagebox.showwarning("Selection Error", "Please select a task.")

# Delete a task
def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        listbox.delete(index)
        save_tasks(tasks)
    else:
        messagebox.showwarning("Selection Error", "Please select a task.")

# Initialize the window
root = tk.Tk()
root.title("To-Do List App")

# Tasks list
tasks = load_tasks()

# GUI Components
frame = tk.Frame(root)
frame.pack(pady=20)

entry = tk.Entry(frame, width=30)
entry.grid(row=0, column=0)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=1)

complete_button = tk.Button(frame, text="Complete Task", command=complete_task)
complete_button.grid(row=1, column=0, columnspan=2, pady=10)

delete_button = tk.Button(frame, text="Delete Task", command=delete_task)
delete_button.grid(row=2, column=0, columnspan=2)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=20)

# Load tasks into the listbox on start
for task in tasks:
    task_display = task["task"]
    if task["completed"]:
        task_display += " - [Completed]"
    listbox.insert(tk.END, task_display)

# Run the main loop
root.mainloop()
