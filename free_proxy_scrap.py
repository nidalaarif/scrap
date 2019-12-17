import time
import requests
import html5lib
from bs4 import BeautifulSoup
import mysql.connector
from pprint import pprint

mydb = mysql.connector.connect(
  host="localhost",
  port="8889",
  user="root",
  passwd="root",
  database="proxies"
)


req = requests.get("https://free-proxy-list.net/","lxml")

proxySoup = BeautifulSoup(req.content,"html5lib")

table = proxySoup.find("table",attrs={"id":"proxylisttable"})

rows = table.find("tbody").find_all("tr")
proxies = []

for row in rows:
    proxy = {}
    cells = row.find_all("td")
    proxy["ip"] = cells[0].text
    proxy["port"] = cells[1].text
    proxy["code"] = cells[2].text
    proxy["country"] = cells[3].text
    proxy["anonym"] = cells[4].text
    proxy["google"] = cells[5].text
    proxy["https"] = cells[6].text

    proxies.append(proxy)

for item in proxies:
    mycursor = mydb.cursor()
    sql = "INSERT INTO proxies_table (ip, port, code, country, anonym, google, https) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (item["ip"],item["port"],item["code"],item["country"],item["anonym"],item["google"],item["https"])
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")





print("DONE!")
print(len(proxies))
