import mysql.connector
from functions import getProxies
import random
from pprint import pprint


p = getProxies(30)
proxies = []

for item in p:
    proxies.append(item[0])


print(proxies[random.randint(0,len(proxies) - 1)])
print(proxies[random.randint(0,len(proxies) - 1)])
print(proxies[random.randint(0,len(proxies) - 1)])