import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.1337xx.to/search/avengers/1/")
soup = BeautifulSoup(page.content, 'html.parser')

pages = []

table = soup.select('div.table-list-wrap > table > tbody')[0]
for rows in table.find_all('tr'):
    tandl = rows.select('td > a')[1]
    title = tandl.text
    link = tandl.get('href')
    seed = rows.select('td')[1].text
    leech = rows.select('td')[2].text
    size = rows.select('td')[4].text
    torr_page = {
        "title": title.strip(),
        "link": link.strip(),
        "seeders": seed.strip(),
        "leechers": leech.strip(),
        "size": size.strip(),
    }
    print(torr_page)
    #pages.append(torr_page)

#print(pages)