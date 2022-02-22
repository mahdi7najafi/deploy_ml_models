import requests

url = 'http://localhost:8080/api'
r = requests.post(url, json = {"x" : ['I love to travel.', 'I hate it']})
print(r.json())