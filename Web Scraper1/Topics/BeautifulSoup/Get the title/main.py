import requests

from bs4 import BeautifulSoup

r = requests.get(input())
soup = BeautifulSoup(r.content, "html.parser")
h = soup.find_all("h1")
print(h[0].text)