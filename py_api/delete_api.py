import requests

url = "https://reqres.in/api/users/2"

res = requests.delete(url, verify=False, timeout=10)

print(res.status_code)
print(res.text)