#import mysql.connector
import requests
import html5lib
from bs4 import BeautifulSoup
#from pprint import pprint
from functions import getImage
movies = []
url = "https://yts.lt/browse-movies"

# reauest the webpage
req = requests.get(url,"lxml")
soup = BeautifulSoup(req.content,'html5lib')

# get last page number
pagination = soup.find("ul",{"class":"tsc_pagination"})
pagesCount = int(pagination.find_all("li")[-3].text)

# get all movies in the page with their titles and release dates
figures = soup.find_all("figure")
titles = soup.find_all("a",{"class":"browse-movie-title"})
years = soup.find_all("div",{"class":"browse-movie-year"})

# loop throught the movies 
for figure,title,year in zip(figures,titles,years):
    figcaption = figure.find("figcaption")
    h4_table = figcaption.find_all("h4")
    getImage(figure.img["src"],title.text)

    movie = {}
    movie["image"] = figure.img["src"]
    movie["rating"] = h4_table[0].text
    movie["category"] = h4_table[1].text
    movie["title"] = title.text
    movie["year"] = year.text
    movie["link"] = title["href"]

    


    movies.append(movie)