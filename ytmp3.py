from pytube import YouTube
from sys import argv
import os

link = input("Paste URL here: ")
yt = YouTube(link)

print("Title: ", yt.title)

dir_path = os.path.dirname(os.path.realpath(__file__))

yd = yt.streams.filter(only_audio=True).first()
out = yd.download(dir_path+'/mp3')

base, ext = os.path.splitext(out)
new_file = base + '.mp3'
os.rename(out, new_file)

print(yt.title + " saved")

input("Press anything to exit...")
