import time
import requests
import html5lib
from bs4 import BeautifulSoup
from pprint import pprint

title = ("Play It to the Bone").lower()
year = "1999"
movieUrl = "https://yts.lt/movie/"+title.replace(" ","-").replace("'","")+"-"+year
movieUrl2 = "https://yts.lt/movie/criminal-2004"
movieRequest = requests.get(movieUrl2,"lxml")
time.sleep(5)
movieSoup = BeautifulSoup(movieRequest.content,'html5lib')

movieInfo = movieSoup.find("div",attrs={"id":"movie-info"})


print(movieRequest.status_code)

