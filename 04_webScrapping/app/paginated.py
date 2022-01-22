import json
from bs4 import BeautifulSoup
from app.constants import PAGINATED_FILE_NAME

from app.fileWriter import writeInfo
from app.utils import getPaginatedUrl


def extractPaginatedInformation(soup: BeautifulSoup, pageNumber):
    cardsDictionary = []
    cards = soup.find_all('div', class_= 'col-lg-4 col-md-6 mb-4')
    
    for card in cards:
        title = card.find('h4').find('a').text
        price = float(card.find('h5').text[1:])
        imgurl = card.find('img')['src']

        cardDictionary = { 'title': title, 'price': price, 'imgurl': imgurl }
        cardsDictionary.append(cardDictionary)
    
    writeInfo(getPaginatedUrl(pageNumber), json.dumps(cardsDictionary,indent = 4))