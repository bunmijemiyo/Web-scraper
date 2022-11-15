import requests

from bs4 import BeautifulSoup

word = input()
r = requests.get(input())
soup = BeautifulSoup(r.content, "html.parser")
paragraph1 = soup.find_all("p")
for i in paragraph1:
    if word in i.text:
        print(i.text)
        break
