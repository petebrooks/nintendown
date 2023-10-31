import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import pyperclip
import re
import scdl
import time

def validate_url(url):
    regex = re.compile(r"^(https?://)?(www\.)?soundcloud\.com/[\w\-/]+$")
    return regex.match(url)


def on_button_click():
    url = pyperclip.paste()
    if url and validate_url(url):
        download_dir = filedialog.askdirectory(title='Select Download Directory')
        if download_dir:
            command = f'cd {download_dir}; scdl -c -l {url}'
            print(f'Command: {command}')
            start_time = time.time()
            print(f'Start time: {time.ctime(start_time)}')
            try:
                subprocess.run(command, shell=True, check=True, stderr=subprocess.PIPE, text=True)
                messagebox.showinfo("Success", "Download completed successfully")
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", e.stderr)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f'End time: {time.ctime(end_time)}')
            print(f'Time elapsed: {elapsed_time} seconds')
        else:
            messagebox.showinfo("Info", "Download cancelled")
    elif not url:
        messagebox.showerror("Error", "No URL found in clipboard")
    else:
        messagebox.showerror("Error", "Invalid SoundCloud URL")


# Create the main window
window = tk.Tk()
window.title("NINTENDOWN")
window.configure(bg="#EED5F7")

# Padding around the button
frame = tk.Frame(window, bg="#EED5F7")
frame.pack(padx=80, pady=80)  # Adjust padding as per your aesthetic preference

# Create a button
button = tk.Button(
    frame,
    text="NINTENDOWNLOAD IT!",
    command=on_button_click,
    relief="flat",
    bg="#EED5F7",
    fg="#000000",
    font=("Arial", 20),
)
button.pack()

# Run the Tkinter event loop
window.mainloop()
