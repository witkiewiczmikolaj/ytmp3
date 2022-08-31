from pytube import YouTube
from sys import argv
from moviepy.editor import *

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download("D:/")

mp4_file = r'D:/3 PYTHON AUTOMATION PROJECTS FOR BEGINNERS.mp4'
mp3_file = r'D:/3 PYTHON AUTOMATION PROJECTS FOR BEGINNERS.mp3'

videoclip = VideoFileClip(mp4_file)
audioclip = videoclip.audio
audioclip.write_audiofile(mp3_file)
audioclip.close()
videoclip.close()