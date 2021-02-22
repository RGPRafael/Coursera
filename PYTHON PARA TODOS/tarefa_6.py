import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter Location: ')
uh =  urllib.request.urlopen(url)
data = uh.read()
info = json.loads(data)
soma = 0
for item in info["comments"]:
    soma = soma + int(item["count"])
print(soma)
