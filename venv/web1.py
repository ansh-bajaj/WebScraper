from bs4 import BeautifulSoup
import requests
search=input("What would you like to search?")
params={"q":search}
r=requests.get("http://bing.com/search",params=params)
soup=BeautifulSoup(r.text,"html.parser")
results=soup.find("div",{"id":"b_content"})
lists=results.findAll("li",{"class": "b_algo"})
for item in lists:
    item_text=item.find("a").text
    item_href=item.find("a").attrs["href"]
    print(item_text)
    print(item_href)
    ## parent parsing
    print("Summary:", item.find("a").parent.parent.find("p").text)
    # child parsing
    #children= item.find("h2")
    #print("Next sibling:",children.next_sibling())
    # for child in children:
        #print(child)