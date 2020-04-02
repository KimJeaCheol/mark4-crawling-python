import requests as rq
import json
from bs4 import BeautifulSoup

url = "https://www.naver.com/"

res = rq.get(url)

print(res)
print(res.status_code)
headers = res.headers

print(headers['Set-Cookie'])

for header in headers:
    print(headers[header])

cookies = res.cookies
print(dict(cookies))

print(res.encoding)

