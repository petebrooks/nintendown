import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import pyperclip
import re
import scdl
import time
import os


def validate_url(url):
    # Check if it's a SoundCloud URL
    soundcloud_regex = re.compile(r"^(https?://)?(www\.)?soundcloud\.com/[\w\-/]+$")
    youtube_regex = re.compile(
        r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/[\w\-?=&/]+$"
    )
    if soundcloud_regex.match(url):
        return "soundcloud"
    elif youtube_regex.match(url):
        return "youtube"
    return None


# TODO: Ask about audio format
def on_button_click():
    url = pyperclip.paste()
    url_type = validate_url(url)
    if url and url_type:
        download_dir = filedialog.askdirectory(title="Select Download Directory")
        if download_dir:
            os.chdir(download_dir)
            if url_type == "soundcloud":
                command = f"scdl -c -l {url}"
            else:  # url_type == "youtube"
                command = f"youtube-dl -x --audio-format aac {url}"
            print(f"Command: {command}")
            start_time = time.time()
            print(f"Start time: {time.ctime(start_time)}")
            try:
                subprocess.run(
                    command, shell=True, check=True, stderr=subprocess.PIPE, text=True
                )
                messagebox.showinfo("Success", "Download completed successfully")
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", e.stderr)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"End time: {time.ctime(end_time)}")
            print(f"Time elapsed: {elapsed_time} seconds")
        else:
            messagebox.showinfo("Info", "Download cancelled")
    elif not url:
        messagebox.showerror("Error", "No URL found in clipboard")
    else:
        messagebox.showerror("Error", "Invalid URL")


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
