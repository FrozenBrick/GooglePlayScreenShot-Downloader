import tkinter as tk
import tkinter.font as tkFont
from os import link, name
from tracemalloc import stop
from typing import final
from urllib.request import urlopen
from bs4 import BeautifulSoup
from yurl import URL
import requests
import easygui
import os
from easygui import *
import sys
import tkinter as tk
import tkinter.font as tkFont
import threading

class App:
    def __init__(self, root):
          #setting title
        root.title("Downloader By Bilawal")
        #setting window size
        width=600
        height=400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GMessage_620=tk.Message(root)
        GMessage_620["bg"] = "#393d49"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_620["font"] = ft
        GMessage_620["fg"] = "#333333"
        GMessage_620["justify"] = "center"
        GMessage_620["text"] = ""
        GMessage_620.place(x=0,y=0,width=600,height=400)

        GLabel_840=tk.Label(root)
        GLabel_840["anchor"] = "center"
        ft = tkFont.Font(family='Times',size=24)
        GLabel_840["bg"] = "#393d49"

        GLabel_840["font"] = ft
        GLabel_840["fg"] = "#ffb800"
        GLabel_840["justify"] = "center"
        GLabel_840["text"] = "Google Play Store Image Downloader"
        GLabel_840["relief"] = "flat"
        GLabel_840.place(x=60,y=90,width=481,height=53)

        GButton_389=tk.Button(root)
        GButton_389["anchor"] = "center"
        GButton_389["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=18)
        GButton_389["font"] = ft
        GButton_389["fg"] = "#000000"
        GButton_389["justify"] = "center"
        GButton_389["text"] = "Start"
        GButton_389.place(x=100,y=225,width=100,height=100)
        GButton_389["command"] = self.GButton_389_command

        GButton_494=tk.Button(root)
        GButton_494["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=18)
        GButton_494["font"] = ft
        GButton_494["fg"] = "#000000"
        GButton_494["justify"] = "center"
        GButton_494["text"] = "Exit"
        GButton_494.place(x=400,y=225,width=100,height=100)
        GButton_494["command"] = self.GButton_494_command

        GLabel_238=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_238["font"] = ft
        GLabel_238["bg"] = "#393d49"
        GLabel_238["fg"] = "#ffffff"
        GLabel_238["justify"] = "center"
        GLabel_238["text"] = "By Bilawal M"
        GLabel_238.place(x=500,y=360,width=79,height=30)

    def GButton_389_command(self):
        value = easygui.enterbox(msg="Paste Full URL", title="BilawalM")
        url = value
        path = 'Images'
        if not os.path.exists(path):
            os.makedirs(path) 
        else:
         None
        #url = "https://play.google.com/store/apps/details?id=com.dts.freefiremax"
        r = requests.get(url)

        soup = BeautifulSoup(r.content, 'html5lib')

        images = soup.find_all("img", alt="Screenshot image")

        imagelinks= []
        for item in images:
            src = item.get("src")
            if src is None or not src.startswith("https://"):
                src = item.get("data-src")
            result = (URL(src).replace(query='-h9999-w9999'))
            imagelinks.append(result)
            for i, imagelink in enumerate(imagelinks):
                response = requests.get(imagelink)
                imagename = "Images" + '/' + "data" + str(i+1) + '.jpg'
                with open(imagename, 'wb') as file:
                        file.write(response.content)         

    def GButton_494_command(self):

        sys.exit()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    
    root.mainloop()




##The Program is developed by BilawalM and has all the rights.



