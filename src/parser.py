import requests
from bs4 import BeautifulSoup

def get_page_soup(url, default=None):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')

    except requests.exceptions.RequestException as e:
        print(f"Error while loading {url}: {e}")
        return default
    