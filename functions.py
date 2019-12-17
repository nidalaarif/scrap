
import requests
import html5lib
from bs4 import BeautifulSoup
import mysql.connector



def getProxies(limit):
    mydb = mysql.connector.connect(
    host="localhost",
    port="8889",
    user="root",
    passwd="root",
    database="proxies"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT concat(ip,':',port) as pro FROM proxies_table	 WHERE https = 'yes' LIMIT "+str(limit))
    proxies = mycursor.fetchall()
    return proxies

def getProxies_live():
    req = requests.get("https://free-proxy-list.net/","lxml")

    proxySoup = BeautifulSoup(req.content,"html5lib")

    table = proxySoup.find("table",attrs={"id":"proxylisttable"})

    rows = table.find("tbody").find_all("tr")
    proxies = []

    for row in rows:
        cells = row.find_all("td")
        if cells[6].text == "yes":
            proxy = cells[0].text+":"+cells[1].text
            proxies.append(proxy)
        

    return proxies

def getImage(img_url,name):
    name = name.replace(" ","_")
    name = name.replace("'","")
    
    with open("images/"+name+".jpg", 'wb') as handle:
        response = requests.get(img_url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)


def proxies_from_file():
    lines = tuple(open("http_proxies.txt", 'r'))
    proxies = []
    for line in lines:
        proxies.append(line.replace("\n",""))

    del lines
    return proxies




