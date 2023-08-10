import csv
import json

header = ['id', 'name', 'lat', 'long']

data = []

with open('./cities.json','r') as file:
    json_data = json.loads(file.read())
    for i in json_data:
        data.append(list(i.values()))

with open('cities.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
