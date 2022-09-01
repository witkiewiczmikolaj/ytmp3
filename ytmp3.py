from cgitb import text
import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import DISABLED, NORMAL, Label
from winreg import REG_WHOLE_HIVE_VOLATILE
from pytube import YouTube
import os

root = tk.Tk()
root.title("YT to MP3")
root.resizable(False, False)
root.iconbitmap("icon.ico")
succ = Label(text="Success!", bg="white", font=("Arial", 8))

def addFolder():

    path = askdirectory(title='Select your folder') 
    pathDisp.config(state=NORMAL)
    pathDisp.delete(0,1000)
    pathDisp.insert(0,path)
    pathDisp.config(state=DISABLED)

def runApp():
    
    succ.after(1000, succ.master.destroy)
    
    link = pasteUrl.get()
    yt = YouTube(link)
    yd = yt.streams.filter(only_audio=True).first()
    out = yd.download(addFolder)

    base, ext = os.path.splitext(out)
    new_file = base + '.mp3'
    os.rename(out, new_file)

    succ.place(width=150, height=10, x=150, y=143)
    

def on_enter_run(e):
   runApps.config(background='#182629')
   
def on_enter_path(e):
   openFolder.config(background='#182629')

def on_leave_run(e):
   runApps.config(background= '#263D42')

def on_leave_path(e):
   openFolder.config(background= '#263D42')

canvas = tk.Canvas(root, height=160, width=500, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(height=150, width=490, x=7, y=7)

openFolder = tk.Button(root, text="Choose folder", padx=10, pady=5, fg="white", bg="#263D42", command=addFolder)
openFolder.place(x=10, y=10)

pathDisp = tk.Entry(root, bg='#e8edea')
canvas.create_window(160, 60, width=300, window=pathDisp)

url = Label(text="Paste URL here:", bg="white", font=("Arial", 15))
url.place(width=150, height=30, x=10, y=90)

pasteUrl = tk.Entry(root, bg='#e8edea')
canvas.create_window(160, 130, width=300, window=pasteUrl)

runApps = tk.Button(root, text="Download MP3", padx=10, pady=50, fg="white", bg="#263D42", font='sans 12 bold', command=runApp)
runApps.place(x=330, y=16)

runApps.bind('<Enter>', on_enter_run)
runApps.bind('<Leave>', on_leave_run)
openFolder.bind('<Enter>', on_enter_path)
openFolder.bind('<Leave>', on_leave_path)

root.mainloop()


