import requests
from bs4 import BeautifulSoup
res = requests.get(
    'https://www.1377x.to/torrent/5347176/Prey-2022-1080p-10bit-WEBRip-6CH-x265-HEVC-PSA/')
txt = res.text
status = res.status_code

soup = BeautifulSoup(txt, 'html.parser')

 
products = soup.select('div.box-info > div')[1]
link = products.select('ul >li> a')[0].get('href')


print(link)