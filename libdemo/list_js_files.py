import requests
from bs4 import BeautifulSoup

URL = "http://www.w3schools.com"

url = input("Enter url :")
resp = requests.get(url)
bs = BeautifulSoup(resp.text,"html.parser")

for script in bs.find_all("script"):

    if 'src' in script.attrs and script['src'].endswith(".js"):
         print( script['src'])







