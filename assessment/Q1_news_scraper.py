import requests
from bs4 import BeautifulSoup

def scrape_latest_news():
    url = 'https://edition.cnn.com/world'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for item in soup.select('.cd__headline-text'):
        title = item.get_text()
        link = item.find_parent('a')['href']
        print(f"Title: {title}, URL: https://cnn.com{link}")

if __name__ == "__main__":
    scrape_latest_news()
