#!/usr/bin/env python3

import json
import requests

response = requests.get("http://api.open-notify.org/astros.json")
print(response)

print()
query = {'lat':'45', 'lon':'180'}
response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
j = response.json()
print(json.dumps(j))

print()
response = requests.get("http://api.open-notify.org/astros.json")
print(json.dumps(response.json(), sort_keys=True, indent=4))

print()
response = requests.post('https://httpbin.org/post', data = {'key':'value'})

print()
requests.put('https://httpbin.org/put', data = {'key':'value'})

if __name__ == "__main__":
    pass