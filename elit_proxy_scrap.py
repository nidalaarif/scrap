import requests
import html5lib
from bs4 import BeautifulSoup
import mysql.connector
from pprint import pprint
import time

mydb = mysql.connector.connect(
  host="localhost",
  port="8889",
  user="root",
  passwd="root",
  database="proxies"
)



req = requests.get("https://www.proxynova.com/proxy-server-list/elite-proxies/","lxml")

proxySoup = BeautifulSoup(req.content,"html5lib")

table = proxySoup.find("table",attrs={"id":"tbl_proxy_list"})

rows = table.find("tbody").find_all("tr")
proxies = []

for row in rows:
  proxy = {}
  cells = row.find_all("td")
  ip = cells[0].find("abbr")
  proxy["ip"] = ip["title"].text
  #proxy["port"] = cells[1].find("a")
  proxies.append(proxy)




print(proxies)

