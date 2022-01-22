# Main Driver Function
from app.basics import extractInformation
from app.constants import PAGINATED_URL, URL
from app.getWebpage import getWebPage
from app.paginated import extractPaginatedInformation


def basicsDriver():
    soup = getWebPage(URL)
    extractInformation(soup)


def paginatedDriver():
    # Get Paggination Urls
    soup = getWebPage(PAGINATED_URL)
    pages = soup.find('ul', class_="pagination")

    urls = [PAGINATED_URL]
    links = pages.find_all('a', class_='page-link')
    for link in links:
        if link.text.isdigit():
            urls.append(PAGINATED_URL + '?page=' + link.text)
    
    # Extract Information From Each Page
    for i in range(len(urls)):
        soupPage = getWebPage(urls[i])
        extractPaginatedInformation(soupPage, i+1)


# basicsDriver()
paginatedDriver()