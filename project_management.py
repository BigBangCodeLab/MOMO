import tkinter as tk
from tkinter import filedialog
import os
import json

def open_vscode(project_path):
    os.system(f'code "{project_path}"')

def open_folder_dialog():
    root = tk.Tk()
    root.withdraw()

    folder_path = filedialog.askdirectory(initialdir="D:\\xampp\\htdocs\\projects")
    return folder_path

def save_project_path(project_name, project_path, storage_file="project_paths.json"):
    if not os.path.exists(storage_file):
        with open(storage_file, 'w') as f:
            json.dump({}, f)
    
    with open(storage_file, 'r+') as f:
        paths = json.load(f)
        paths[project_name] = project_path
        f.seek(0)
        json.dump(paths, f, indent=4)

def get_project_path(project_name, storage_file="project_paths.json"):
    if os.path.exists(storage_file):
        with open(storage_file, 'r') as f:
            paths = json.load(f)
            return paths.get(project_name)

