
import requests
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




