import requests
import scrapy

url = 'https://brickset.com/sets/year-2009'
req = requests.get(url)
print(req.text)

print("Status code:")
print("\t *", req.status_code)

h = requests.head(url)
print("Header:")
print("**********")

for line in h.headers:
    print("\t", line, ":", h.headers[line])
print("**********")

headers = {
    'User-Agent': 'Mobile'
}
modified_ua = requests.get(url, headers=headers)
print(modified_ua.request.headers)
print("**************")
