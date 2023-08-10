import requests
from bs4 import BeautifulSoup
import time
import json

data = []

for i in range(1,562):
    print(i)
    response = requests.get("https://geokeo.com/database/city/{}/".format(i)).text
    soup = BeautifulSoup(response,'lxml')
    for j in soup.tbody.find_all('tr'):
        ls = j.find_all('td')
        data.append({
            'id': ls[0].text,
            'name': ls[1].text,
            'lat': ls[3].text,
            'long': ls[4].text
        })
        del j, ls
    del response, soup
    time.sleep(3)

with open('cities.json','w') as file:
    json.dump(data,file,ensure_ascii=False)
    file.close()
del data
