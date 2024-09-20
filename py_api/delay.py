url = "https://httpbin.org/delay/2"

import requests

res = requests.delete(url, timeout=1, verify=False)
print(res.status_code)
