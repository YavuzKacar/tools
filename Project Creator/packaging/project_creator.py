import os
from pathlib import Path
import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime

def create_project(task_id, description, root_path):
    base_dir = Path(root_path) / task_id
    if base_dir.exists():
        messagebox.showwarning("Warning", f"Directory '{base_dir}' already exists.")
        return

    # Folder structure (without .github)
    structure = [
        # ".github",  # removed
        "docs",
        "src",
        "tests",
        "scripts",
        "data",
        "assets"
    ]

    # Create folders
    for folder in structure:
        (base_dir / folder).mkdir(parents=True, exist_ok=True)

    # Create common files (removed .env.example and .gitignore)
    # (base_dir / ".env.example").write_text("# Example environment variables\n")  # removed
    # (base_dir / ".gitignore").write_text("__pycache__/\n*.pyc\n.env\n")  # removed
    (base_dir / "requirements.txt").touch()
    (base_dir / "LICENSE").write_text("MIT License\n")
    (base_dir / "pyproject.toml").write_text(f"[project]\nname = \"{task_id.lower().replace('-', '_')}\"\n")
    creation_date = datetime.now().strftime("%Y-%m-%d")
    readme_content = f"# {task_id}\n\n{description.strip()}\n\n**Project created:** {creation_date}\n"
    (base_dir / "README.md").write_text(readme_content)

    messagebox.showinfo("Success", f"Project '{task_id}' created at:\n{base_dir}")

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path_var.set(folder)

def on_submit():
    task_id = task_id_entry.get().strip()
    description = description_text.get("1.0", tk.END).strip()
    folder_path = folder_path_var.get().strip()

    if not task_id or not description or not folder_path:
        messagebox.showerror("Error", "Please fill in all fields and select a save location.")
        return

    create_project(task_id, description, folder_path)

# GUI Setup
root = tk.Tk()
root.title("Freelance Project Folder Creator")
root.geometry("450x380")
root.resizable(False, False)

# Modern color palette
BG_COLOR = "#23272f"
FG_COLOR = "#f5f6fa"
ENTRY_BG = "#2d323e"
ENTRY_FG = "#f5f6fa"
BTN_BG = "#4f8cff"
BTN_FG = "#ffffff"
BTN_ACTIVE_BG = "#357ae8"
FRAME_BG = BG_COLOR

root.configure(bg=BG_COLOR)

# Task ID
tk.Label(root, text="Jira Task ID:", font=("Arial", 12), bg=BG_COLOR, fg=FG_COLOR).pack(pady=(15, 5))
task_id_entry = tk.Entry(root, font=("Arial", 12), width=35, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=ENTRY_FG, relief=tk.FLAT)
task_id_entry.pack()

# Description
tk.Label(root, text="Project Description:", font=("Arial", 12), bg=BG_COLOR, fg=FG_COLOR).pack(pady=(15, 5))
description_text = tk.Text(root, font=("Arial", 11), height=5, width=40, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=ENTRY_FG, relief=tk.FLAT)
description_text.pack()

# Folder selection
tk.Label(root, text="Select Save Location:", font=("Arial", 12), bg=BG_COLOR, fg=FG_COLOR).pack(pady=(15, 5))
folder_path_var = tk.StringVar()
folder_frame = tk.Frame(root, bg=FRAME_BG)
folder_entry = tk.Entry(folder_frame, textvariable=folder_path_var, font=("Arial", 11), width=28, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=ENTRY_FG, relief=tk.FLAT)
folder_entry.pack(side=tk.LEFT, padx=5)
browse_btn = tk.Button(folder_frame, text="Browse", command=select_folder, bg=BTN_BG, fg=BTN_FG, activebackground=BTN_ACTIVE_BG, activeforeground=BTN_FG, relief=tk.FLAT)
browse_btn.pack(side=tk.LEFT)
folder_frame.pack()

# Submit button
submit_btn = tk.Button(root, text="Create Project", font=("Arial", 12, "bold"), command=on_submit, bg=BTN_BG, fg=BTN_FG, activebackground=BTN_ACTIVE_BG, activeforeground=BTN_FG, relief=tk.FLAT)
submit_btn.pack(pady=20)

root.mainloop()
