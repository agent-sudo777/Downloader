#!/usr/python

import os
import time

os.system("clear")
os.system("pip install youtube_dl")
os.system("apt install figlet")
os.system("apt install jp2a")
os.system("clear")
print("\033[1;36;40m")
print("<+++++This tool is created by b3rd%20mw01u for downloading audios and videos from YouTube+++++>")
os.system("figlet Downloader")

print("\033[1;33;40m")
print("Enter 1 for download mp4\n")
print("Enter 2 for download mp3\n")
print("\033[1;34;40m")
u_choice=int(input("Enter your choice : "))


if u_choice==1:

   print("You have been entered 1\n")
   time.sleep(2)
   os.system("clear")
   os.system("python mp4.py")


if u_choice==2:
  
   print("you have been  entered 2\n")
   time.sleep(2)
   os.system("clear")
   os.system("python mp3.py")

print("by")
os.system("figlet TEAM404")
