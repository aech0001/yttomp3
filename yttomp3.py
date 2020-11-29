from pytube import YouTube
import tkinter as tk
from tkinter import messagebox
#this thing
downloadcomplete = False

#tkinter window
window_main = tk.Tk(className=" YouTube Downloader")
window_main.geometry("400x400")
window_main.configure(bg="#3A84FA")

linkentry = tk.StringVar()
linkentry_widget = tk.Entry(window_main, textvariable=linkentry, width=30,bg="#A9C9FC").place(relx = 0.5, rely = 0.25, anchor = tk.CENTER)
linklabel_widget = tk.Label(window_main, text="Youtube Link:",bg="#3A84FA").place(relx = 0.5, rely = 0.125, anchor = tk.CENTER)

def mp4_function():
    link = linkentry.get()
    maybevalid = link.startswith('https://www.youtube.com/watch?')
    if maybevalid == True:
        ()
    else:
        messagebox.showerror("Error!", "Your link is invalid. Make sure it starts with 'https://www.youtube.com/watch?'")

    yt=YouTube(linkentry.get())
    stream_mp4 = yt.streams.first() #mp4
    stream_mp4.download()

downloadcomplete = True
mp4_submit = tk.Button(window_main, text="Download!",height="3",width="20", command=mp4_function).place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

if downloadcomplete == True:
    downloadcomplete_widget = tk.Label(window_main, text="Download Complete.").place(relx = 0.5, rely = 0.85, anchor = tk.CENTER)
else:
    ()
window_main.mainloop()
