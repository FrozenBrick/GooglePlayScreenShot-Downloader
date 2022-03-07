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


value = easygui.enterbox(msg="Paste Full URL", title="BilawalM")
output = easygui.choicebox()
path = 'Images'
if not os.path.exists(path):
    os.makedirs(path) 
#url = value
url = "https://play.google.com/store/apps/details?id=com.nekki.shadowfightarena"
htmldata = urlopen(url)
soup = BeautifulSoup(htmldata, 'html.parser')
images = soup.find_all('img', alt="Screenshot Image")
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
      print(response)
      #with open(imagename, 'wb') as file:
        #    file.write(response.content)
       #     msg = "Do you want to continue?"
      #      title = "Please Confirm"
     # if ccbox(msg, title):     # show a Continue/Cancel dialog
      #  pass  # user chose Continue
     # else:  # user chose Cancel
         #exit(0)

#easygui.msgbox("Finshed!", ok_button="OK")     


   