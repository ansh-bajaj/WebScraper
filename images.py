from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup
import requests
import os
def StartSearch():
    search=input("What would you like to search?")
    params={"q":search}
    if not os.path.isdir(search):
        os.makedirs(search)
    r=requests.get("http://bing.com/images/search",params=params)
    soup=BeautifulSoup(r.text,"html.parser")
    links=soup.findAll("a",{"class":"thumb"})

    for item in links:
        try:
            img_obj=requests.get(item.attrs["href"])   #converting href
            print("Getting:",item.attrs["href"])
            title=item.attrs["href"].split("/")[-1]
            #[-1]--> last element
            try:
                img=Image.open(BytesIO(img_obj.content))
                img.save("./"+ search +"/"+title,img.format)
            except:
                print("Could not save Image.")
        except:
            print("Could not request Image.")
    StartSearch()

StartSearch()