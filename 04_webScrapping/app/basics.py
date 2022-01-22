# Extract Interested Information
from bs4 import BeautifulSoup
from app.constants import FILE_NAME
from app.fileWriter import writeInfo


def extractInformation(soup: BeautifulSoup):
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    tags = soup.find_all('div', class_='tags')

    info = ''
    for i in range(len(quotes)):
        quoteTags = tags[i].find_all('a', class_='tag')
        info += authors[i].text + '\n' + quotes[i].text
        for tag in quoteTags:
            info += '\n' + "- " + tag.text
        info += '\n\n'
    
    writeInfo(FILE_NAME, info)