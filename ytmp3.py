import tkinter as tk
from tkinter import filedialog, Text
from pytube import YouTube
from sys import argv
import os

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
