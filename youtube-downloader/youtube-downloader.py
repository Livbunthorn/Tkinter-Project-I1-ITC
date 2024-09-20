from tkinter import *
import yt_dlp 
from tkinter import messagebox, filedialog

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Warning", "Please enter a URL.")
        return
    
    # Ask the user to choose a directory to save the video
    download_path = filedialog.askdirectory()
    if not download_path:
        messagebox.showwarning("Warning", "Please select a download location.")
        return
    
    # Set download options
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
    }

    # Download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    # Show success message
    messagebox.showinfo("Success", "Download completed successfully!")


win = Tk()
win.title("YouTube Video Downloader")
win.geometry("400x300")

# Create a label and entry for the URL
url_label = Label(win, text="YouTube URL:")
url_label.pack()

url_entry = Entry(win, width=50)
url_entry.pack()

# Create a download button
download_button = Button(win, text="Download Video", command=download_video)
download_button.pack()


win.mainloop()
