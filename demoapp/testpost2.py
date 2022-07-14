#curl -d '<p>hello bitches</p>' -H 'Content-Type: text/html' http://0.0.0.0:5000/movies

#curl -d '{"name":"coolio"}' -H 'Content-Type: application/json' http://0.0.0.0:5000/movies


import requests
import json

f = open("testRohan.txt", "r", encoding="utf8")

# res = requests.post('http://0.0.0.0:5000/movies', data=json.dumps({"name":"www.google.com"}), headers = {'content-type': 'application/json'})
# res = requests.post('http://0.0.0.0:5000/movies', data=f.read().encode('utf-8'), headers = {'content-type': 'text/html'})
# res = requests.post('http://0.0.0.0:5000/movies', data=json.dumps({"url": "www.google.com", "html": f.read().encode('utf-8')}), headers = {'content-type': 'text/html'})
rawHtml = f.read()
print(rawHtml[:10])
test = rawHtml[:10]
# res = requests.post('http://0.0.0.0:5000/movies', data=json.dumps({"name": "www.gooogle.com", "html": rawHtml}), headers = {'content-type': 'application/json'})
res = requests.post('http://127.0.0.1:8000', data=rawHtml.encode('utf-8'), headers = {'content-type': 'text/html', 'charset': 'utf-8'})


#data=f.read().encode('utf-8')

print(res.text)
