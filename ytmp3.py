import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import DISABLED, NORMAL, Label
from pytube import YouTube
import os
import time

# Setting app title, icon and disabling possibility to resize window.  
root = tk.Tk()
root.title("YT to MP3")
root.resizable(False, False)
root.iconbitmap("icon.ico")

# Choosing directory
def addFolder():

    addFolder.path = askdirectory(title='Select your folder') 
    pathDisp.config(state=NORMAL)
    pathDisp.delete(0,1000)
    pathDisp.insert(0,addFolder.path)
    pathDisp.config(state=DISABLED)
    
# Downloading yt video with sound only and renaming it to .mp3 file
def runApp():

    link = pasteUrl.get()
    yt = YouTube(link)
    yd = yt.streams.filter(only_audio=True).first()
    out = yd.download(addFolder.path)

    base, ext = os.path.splitext(out)
    new_file = base + '.mp3'
    os.rename(out, new_file)

    succ = Label(text="Success!", bg="white", font=("Arial", 8))
    succ.place(width=150, height=10, x=150, y=143)     
    root.after(3000, lambda: succ.destroy()) 
    
# Hovering over buttons changes color
def on_enter_run(e):
   runApps.config(background='#182629')   
def on_enter_path(e):
   openFolder.config(background='#182629')
def on_leave_run(e):
   runApps.config(background= '#263D42')
def on_leave_path(e):
   openFolder.config(background= '#263D42')

# Setting canvas
canvas = tk.Canvas(root, height=160, width=500, bg="#263D42")
canvas.pack()

# Setting frame
frame = tk.Frame(root, bg="white")
frame.place(height=150, width=490, x=7, y=7)

# Setting button to choose directory
openFolder = tk.Button(root, text="Choose folder", padx=10, pady=5, fg="white", bg="#263D42", command=addFolder)
openFolder.place(x=10, y=10)

# Setting input box for directory
pathDisp = tk.Entry(root, bg='#e8edea')
canvas.create_window(160, 60, width=300, window=pathDisp)

# Setting text
url = Label(text="Paste URL here:", bg="white", font=("Arial", 15))
url.place(width=150, height=30, x=10, y=90)

# Setting input box for URL
pasteUrl = tk.Entry(root, bg='#e8edea')
canvas.create_window(160, 130, width=300, window=pasteUrl)

# Setting button to download
runApps = tk.Button(root, text="Download MP3", padx=10, pady=50, fg="white", bg="#263D42", font='sans 12 bold', command=runApp)
runApps.place(x=330, y=16)

# Hovering over buttons changes color
runApps.bind('<Enter>', on_enter_run)
runApps.bind('<Leave>', on_leave_run)
openFolder.bind('<Enter>', on_enter_path)
openFolder.bind('<Leave>', on_leave_path)

root.mainloop()


