import youtube_dl
import os

print("\033[1;32;40m")
os.system("clear")
print("\n\nWelcome to youtube audio downloader\n\n")

os.system("jp2a yt.png")
print("\n\n")
u_url=input("Enter the youtube url : ")
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([u_url])
