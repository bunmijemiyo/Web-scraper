import os

import requests
import string
from bs4 import BeautifulSoup


class Internet:
    def __init__(self, web):
        self.web = web

    def connect(self):
        r = requests.get(self.web)
        if r.status_code == 200 and "content" in r.json():
            print(r.json()['content'])
        else:
            print("Invalid quote resource!")

    def print_page(self):
        re = requests.get(self.web, headers={'Accept-Language': 'en-US,en;q=0.5'})
        if re.status_code == 200:
            soups = BeautifulSoup(re.content, "html.parser")
            descriptions = soups.find("div", class_="summary_text")
            if descriptions:
                print({"title": soups.find("title").text, "description": " ".join(descriptions.text.split())})
            else:
                print('Invalid movie page!')
        else:
            print('Invalid movie page!')

    def bin_file(self):
        address = requests.get(self.web)
        if address.status_code == 200:
            page_content = address.content
            with open("source.html", "wb") as file:
                file.write(page_content)
            print("Content saved.")
        else:
            print(f"The URL returned {address.status_code}!")

    def real_web(self):
        r = requests.get(self.web)
        soup = BeautifulSoup(r.content, 'html.parser')
        article = soup.find_all("article")

        for i in article:
            r_news = i.find('span', class_="c-meta__type")
            if "News" in r_news:
                find_link = i.find('a')  # , {'data-track-action': 'view article'})
                # print(find_link)
                tail = find_link.get('href')
                new_link = "https://www.nature.com" + tail
                r_sub = requests.get(new_link, headers={'Accept-Language': 'en-US,en;q=0.5'})
                soup_2 = BeautifulSoup(r_sub.content, 'html.parser')
                title = soup_2.find("title").text.strip()
                # removing punctuation
                tabl = str.maketrans(dict.fromkeys(string.punctuation))
                tab = title.translate(tabl)
                # replacing spaces by _
                final_title = tab.translate(title.maketrans(' ', '_'))
                if 'images' not in title:
                    body = soup_2.find('div', class_="article__body").text.strip()
                    file = open(f'{final_title}.txt', 'a', encoding='utf-8')
                    file.write(body)
                    file.close()

    def multiple_pages(self):
        page_range = int(input("Pls enter the page range: "))
        article_type = input("Pls enter the article type: ")
        directory = os.getcwd()
        for xx in range(1, page_range + 1):
            r = requests.get(f"https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page={xx}")
            soupd = BeautifulSoup(r.content, "html.parser")
            articles = soupd.find_all("article")
            for i in articles:
                r_news = i.find('span', class_="c-meta__type")
                # (r_news)
                if article_type in r_news:
                    find_link = i.find('a')  # , {'data-track-action': 'view article'})
                    # print(find_link)

                    tail = find_link.get('href')
                    new_link = "https://www.nature.com" + tail
                    # print(new_link)
                    r_sub = requests.get(new_link, headers={'Accept-Language': 'en-US,en;q=0.5'})
                    soup_2 = BeautifulSoup(r_sub.content, 'html.parser')
                    title = soup_2.find("title").text.strip()
                    # removing punctuation
                    tabl = str.maketrans(dict.fromkeys(string.punctuation))
                    tab = title.translate(tabl)
                    # print(tab)
                    # replacing spaces by _
                    final_title = tab.translate(title.maketrans(' ', '_'))
                    # print(body)
                    os.makedirs(directory + f"\Page_{xx}", exist_ok=True)
                    os.chdir(directory + f"\Page_{xx}")
                    if 'images' not in title:
                        # os.makedirs(directory + f"\Page_{xx}", exist_ok=True)
                        # os.chdir(directory + f"\Page_{xx}")
                        try:
                            body = soup_2.find('div', class_="article__body").text.strip()
                            # os.makedirs(directory + f"\Page_{xx}", exist_ok=True)
                            # os.chdir(directory + f"\Page_{xx}")
                            # file = open(f'{os.path.join(str(xx), final_title)}.txt', 'w', encoding='utf-8')
                            # file = open(f"{os.path.join(directory, 'Page_' + str(xx), final_title + '.txt')}")
                            file = open(f"{final_title.replace('__Research_Highlights', '')}.txt", "w",
                                        encoding="utf-8")
                            file.write(body)
                            # os.chdir(directory)
                            file.close()
                            os.chdir(directory)

                        except AttributeError:
                            body = soup_2.find('div', class_="article-item__body").text.strip()
                            # os.makedirs(directory + f"\Page_{xx}", exist_ok=True)
                            # os.chdir(directory + f"\Page_{xx}")
                            # file = open(os.path.join(r"C:\\Users\\OGUNJEMIYO OLUBUNMI\\PycharmProjects\\Web Scraper1\\Web Scraper\\task\\Page_" + str(xx), final_title) + ".txt", 'w', encoding='utf-8')
                            file = open(f"{final_title.replace('__Research_Highlights', '')}.txt", "w",
                                        encoding="utf-8")
                            # file = open(f"{os.path.join(directory, 'Page_' + str(xx), final_title + '.txt')}")
                            # file = open(os.path.join("Page_" + str(xx), final_title) + ".txt")
                            file.write(body)
                            # os.chdir(directory)
                            file.close()
                            os.chdir(directory)
        # os.chdir(directory)
        print("Saved all articles.")


# w3 = Internet("https://www.nature.com/nature/articles")
# w3.connect()
# w3.print_page()
# w3.bin_file()
# w3.real_web()
# w3.multiple_pages()

# print(os.getcwd())


def multiple_page():
    page_range = int(input("Pls enter the page range: "))
    article_type = input("Pls enter the article type: ")
    directory = os.getcwd()
    for xx in range(1, page_range + 1):
        r = requests.get(f"https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page={xx}")
        soupd = BeautifulSoup(r.content, "html.parser")
        articles = soupd.find_all("article")
        for i in articles:
            r_news = i.find('span', class_="c-meta__type")
            if article_type in r_news:
                find_link = i.find('a')  # , {'data-track-action': 'view article'})
                tail = find_link.get('href')
                new_link = "https://www.nature.com" + tail
                r_sub = requests.get(new_link, headers={'Accept-Language': 'en-US,en;q=0.5'})
                soup_2 = BeautifulSoup(r_sub.content, 'html.parser')
                title = soup_2.find("title").text.strip()
                # removing punctuation
                tabl = str.maketrans(dict.fromkeys(string.punctuation))
                tab = title.translate(tabl)
                # replacing spaces by _
                final_title = tab.translate(title.maketrans(' ', '_'))
                # Creating directory if it doesn't exist
                os.makedirs(directory + f"\Page_{xx}", exist_ok=True)
                os.chdir(directory + f"\Page_{xx}")
                if 'images' not in title:
                    try:
                        body = soup_2.find('div', class_="article__body").text.strip()
                        file = open(f"{final_title.replace('__Research_Highlights', '')}.txt", "w", encoding="utf-8")
                        file.write(body)
                        file.close()
                        os.chdir(directory)

                    except AttributeError:
                        body = soup_2.find('div', class_="article-item__body").text.strip()
                        file = open(f"{final_title.replace('__Research_Highlights', '')}.txt", "w", encoding="utf-8")
                        file.write(body)
                        file.close()
                        os.chdir(directory)

            else:
                os.makedirs(directory + f"\Page_{xx}", exist_ok=True)
                os.chdir(directory + f"\Page_{xx}")
                os.chdir(directory)

    print("Saved all articles.")


multiple_page()

# a = 'femilola'.replace("lola", "")
# print(a)
