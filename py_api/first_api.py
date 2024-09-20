import requests
url = "https://reqres.in/api/unknown/2"
# res = requests.get("https://reqres.in/api/users?page=2", verify=False)
p = {"page": 2}
# res = requests.get("https://reqres.in/api/users/", verify=False, params=p)

res = requests.get(url, verify=False)
print(res.status_code)

print(res.headers)
print(res.url)
print(res.encoding)

#prints data
print(type(res.json()), res.json())
print(type(res.text), res.text)
print(type(res.content), res.content)
print("history", res.history, "links", res.links)
print(dir(res))