from bs4 import BeautifulSoup
import requests
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scraper.settings")
django.setup()

from ScraperData.models import News

def scraper():
    url = "https://www.imdb.com/news/top/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url ,headers=headers)


    soup = BeautifulSoup(response.text , "html.parser")
    
    artical = []

    new_items = soup.find_all('div', class_="ipc-list-card--border-line ipc-list-card--base ipc-list-card sc-81fd776b-0 bMblhd")

    for item in new_items:
        titel = item.find('a',class_="ipc-link ipc-link--base sc-81fd776b-2 gnCMu")
        description = item.find('div', class_="ipc-html-content-inner-div")
        images = item.find('img',class_="ipc-image")
        external_link = titel['href']
        
        titel = titel.text.strip() if titel else "No Titel"
        description = description.text if description else "No description"
        images = images['src']

        artical.append({
            titel:"titel",
            description:"description",
            images:"images",
            external_link:"external_link",
        })

        News.objects.create(
            titel=titel,
            description=description,
            images=images,
            external_link=external_link
        )


        




scraper()



