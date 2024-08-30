import os
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

def open_multiple_instances(app_path, instance_count):
    for _ in range(instance_count):
        subprocess.Popen([app_path])

def browse_file():
    app_path = filedialog.askopenfilename(
        title="Select Application",
        filetypes=(("Executable Files", "*.exe"), ("All Files", "*.*"))
    )
    app_entry.delete(0, tk.END)
    app_entry.insert(0, app_path)

def on_submit():
    app_path = app_entry.get()
    try:
        instance_count = int(instance_entry.get())
        open_multiple_instances(app_path, instance_count)
        messagebox.showinfo("Success", f"Opened {instance_count} instances of the application.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of instances.")

# Setting up the GUI
root = tk.Tk()
root.title("Open Multiple Instances")

tk.Label(root, text="Application Path").pack(pady=10)
app_entry = tk.Entry(root, width=50)
app_entry.pack(pady=5)

tk.Button(root, text="Browse", command=browse_file).pack(pady=5)

tk.Label(root, text="Number of Instances").pack(pady=10)
instance_entry = tk.Entry(root, width=10)
instance_entry.pack(pady=5)

tk.Button(root, text="Open Instances", command=on_submit).pack(pady=20)

root.mainloop()
