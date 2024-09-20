import json

import requests
url = "https://reqres.in/api/users/2"
payload = {
    "name": "Naga",
    "job": "Vilan"
}

res = requests.put(url, data=payload, verify=False)
print(res.status_code)
print(res.json())


got = requests.patch(url, data=json.loads(open("user.json").read()), verify=False)
print(got.status_code)
print(got.json())
