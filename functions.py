
import requests

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




