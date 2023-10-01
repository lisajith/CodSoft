import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
        
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")
        
def clear_tasks():
    listbox.delete(0,tk.END,)
    
root = tk.Tk()
root.title("To-Do List")

heading_label = tk.Label(root, text="To-Do List", font=("Helvetica", 18, "bold"))

entry = tk.Entry(root, width=30, bg="pink")
add_button = tk.Button(root, text="Add Task", bg="skyblue", command=add_task)
remove_button = tk.Button(root, text="Remove Task", bg="red", command=remove_task)
clear_button = tk.Button(root, text="Clear All", bg="darkgreen", command=clear_tasks)
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50)

heading_label.pack(pady=10)
entry.pack(pady=10)
add_button.pack()
remove_button.pack()
clear_button.pack()
listbox.pack()


root.mainloop()
