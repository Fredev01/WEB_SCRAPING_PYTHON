import requests

from lxml import html
encabezdo = {
    "user-agent": "Mozilla/5.0 (x11;Linux x86_64) AppleWebkit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Safari/537.36",

}
url: str = "https://www.amazon.com.mx/"
response = requests.get(url, headers=encabezdo)

print(response.text)
