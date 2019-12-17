from pprint import pprint
lines = tuple(open("http_proxies.txt", 'r'))
proxies = []
for line in lines:
    proxies.append(line.replace("\n",""))

del lines
pprint(proxies)
