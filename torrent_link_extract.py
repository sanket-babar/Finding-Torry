import requests
from bs4 import BeautifulSoup
res = requests.get(
    'https://www.1337xx.to/torrent/3911065/Avengers-Endgame-2019-WEBRip-1080p-YTS-YIFY/')
txt = res.text
status = res.status_code

soup = BeautifulSoup(txt, 'html.parser')

 
data = soup.select('div.box-info > div')[1]
title = soup.select('div.box-info > div > h1')[0].text
link = data.select('ul >li> a')[0].get('href')
li2 = data.select('ul.list')[0].select('li')[3]
li3 = data.select('ul.list')[1].select('li')[3]
li4 = data.select('ul.list')[1].select('li')[4]
size = li2.select('span')[0].text
seed = li3.select('span')[0].text
leech = li4.select('span')[0].text
title = soup.select('div.box-info > div > h1')[0].text

print(link +'  '+ size + "  "+ seed + "  "+leech)