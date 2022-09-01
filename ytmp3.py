
from fileinput import filename
import tkinter as tk
from tkinter import filedialog, Text
from winreg import REG_WHOLE_HIVE_VOLATILE
from pytube import YouTube
import os

root = tk.Tk()

def addFolder():
    filename = filedialog.askopenfilename(initialdir="/", title="Select Folder", filetypes=(("executables", ".exe"), ("all files", "*.*")))

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFolder = tk.Button(root, text="Open folder", padx=10, pady=5, fg="white", bg="#263D42", command=addFolder)

openFolder.pack()

runApp = tk.Button(root, text="Run App", padx=10, pady=5, fg="white", bg="#263D42")

runApp.pack()

root.mainloop()
'''
link = input("Paste URL here: ")
yt = YouTube(link)

print("Title: ", yt.title)

yd = yt.streams.filter(only_audio=True).first()
out = yd.download("D:/")

base, ext = os.path.splitext(out)
new_file = base + '.mp3'
os.rename(out, new_file)

print(yt.title + " saved")

input("Press anything to exit...")

'''

