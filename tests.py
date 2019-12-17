import time
import requests
import html5lib
import random
from bs4 import BeautifulSoup
from pprint import pprint
from functions import proxies_from_file



proxies = proxies_from_file()

url = "https://yts.lt/movie/criminal-2004"
for i in range(1,len(proxies)):
    proxy = proxies[i-1]
    print("Request #%d"%i)
    try:
        response = requests.get(url,proxies={"http": proxy, "https": proxy})
        print(response.json())
    except:
        print("Skipping. Connnection error")

proxy = proxies[random.randint(0,len(proxies) - 1)]
title = ("Play It to the Bone").lower()
year = "1999"
movieUrl = "https://yts.lt/movie/"+title.replace(" ","-").replace("'","")+"-"+year
movieUrl2 = "https://yts.lt/movie/criminal-2004"
#movieRequest = requests.get(movieUrl2, proxies={"http": proxy, "https": proxy})
#movieSoup = BeautifulSoup(movieRequest.content,'html5lib')

#movieInfo = movieSoup.find("div",attrs={"id":"movie-info"})


#print(movieRequest.status_code)

