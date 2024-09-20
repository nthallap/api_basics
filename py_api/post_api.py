import json

import requests
url = "https://reqres.in/api/users"
payload = {
    "name": "Naga",
    "job": "Hero"
}

res = requests.post(url, data=payload, verify=False)
print(res.status_code)
print(res.json())


got = requests.post(url, data=json.loads(open("user.json").read()), verify=False)
print(got.status_code)
print(got.json())
