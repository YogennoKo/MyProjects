from pytube import YouTube
from sys import argv

link = input("Input your link: ")
#folder = input("Input the folder for saving: ")
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('/Users/paUpAu/Documents/Youtube')