import requests

from bs4 import BeautifulSoup
num = int(input())
url = input()
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
h = soup.find_all("h2")
print(h[num].text)