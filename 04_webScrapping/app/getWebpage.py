import requests
from bs4 import BeautifulSoup

# Get Webpage in Lxml format using requests and beautifulsoup
def getWebPage(url: str) -> BeautifulSoup:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup