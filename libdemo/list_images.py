import requests
from bs4 import BeautifulSoup

URL = "http://www.w3schools.com"

url = input("Enter url :")
resp = requests.get(url)
bs = BeautifulSoup(resp.text, "html.parser")

for img in bs.find_all("img"):
    if 'src' in img.attrs:
        print(img['src'])
