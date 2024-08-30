import os
import tkinter as tk
from tkinter import filedialog, messagebox

def open_multiple_instances(app_path, instance_count):
    bash_script = f"""
    #!/bin/bash
    for i in {{1..{instance_count}}}
    do
       open -n -a "{app_path}"
    done
    """
    
    script_path = "/tmp/open_apps.sh"
    
    with open(script_path, "w") as file:
        file.write(bash_script)
    
    os.chmod(script_path, 0o755)
    os.system(script_path)

def browse_file():
    app_path = filedialog.askopenfilename(
        title="Select Application",
        filetypes=(("Applications", "*.app"), ("All Files", "*.*"))
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
