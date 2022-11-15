import requests


def do_search(bookstore_url, params):
    # r = requests.get('http://bookstore.com/search', "params = {'author': 'Austen', 'title': 'Emma'}")
    return requests.get(bookstore_url, params)
