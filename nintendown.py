import tkinter as tk
from tkinter import ttk  # For Progressbar
from tkinter import messagebox, filedialog
import subprocess
import threading
import pyperclip
import re
import os


def validate_url(url):
    soundcloud_regex = re.compile(r"^(https?://)?(www\.)?soundcloud\.com/[\w\-/]+$")
    youtube_regex = re.compile(
        r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/[\w\-?=&/]+$"
    )
    if soundcloud_regex.match(url):
        return "soundcloud"
    elif youtube_regex.match(url):
        return "youtube"
    return None


def download_audio(url, url_type, download_dir):
    # Start the progress bar
    progress_bar.start()

    if url_type == "soundcloud":
        command = f"scdl -c -l {url}"
    else:  # url_type == "youtube"
        command = f"youtube-dl -x --audio-format mp3 {url}"

    try:
        subprocess.run(
            command, shell=True, check=True, stderr=subprocess.PIPE, text=True
        )
        messagebox.showinfo("Success", "Download completed successfully")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", e.stderr)

    # Stop the progress bar
    progress_bar.stop()


def on_button_click():
    url = pyperclip.paste()
    url_type = validate_url(url)
    if url and url_type:
        download_dir = filedialog.askdirectory(title="Select Download Directory")
        if download_dir:
            os.chdir(download_dir)
            start_download_thread(url, url_type, download_dir)
        else:
            messagebox.showinfo("Info", "Download cancelled")
    elif not url:
        messagebox.showerror("Error", "No URL found in clipboard")
    else:
        messagebox.showerror("Error", "Invalid URL")


def start_download_thread(url, url_type, download_dir):
    download_thread = threading.Thread(
        target=download_audio, args=(url, url_type, download_dir)
    )
    download_thread.start()


# GUI setup
window = tk.Tk()
window.title("NINTENDOWN")
window.configure(bg="#EED5F7")

frame = tk.Frame(window, bg="#EED5F7")
frame.pack(padx=80, pady=80)

# Add an indeterminate progress bar
progress_bar = ttk.Progressbar(
    frame, orient="horizontal", length=300, mode="indeterminate"
)
progress_bar.pack()

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
