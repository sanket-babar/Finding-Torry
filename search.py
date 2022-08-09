import requests
from bs4 import BeautifulSoup

class Search:
  def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.3'}
        self.url = 'https://www.1337xx.to/search/'

  def key_words_search_words(self, user_message):
    words = user_message.split()[1:]
    keywords = '%20'.join(words)
    search_words = ' '.join(words)
    firstpage = keywords+'/1/'
    return firstpage, search_words

  def search(self, firstpage):
    response = requests.get(self.url+firstpage, headers = self.headers)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    result_links = soup.findAll('a')
    return result_links
      
  def send_link(self, result_links, search_words): 
    send_link = []
    for link in result_links:
        text = link.text.lower()
        if search_words in text:  
            send_link.append('http://1337xx.to'+link.get('href'))
    return send_link

  def magnet(self,send_link):
    magnet_link = []
    seeders = []
    leechers = []
    title = []
    size = []
    x = min(5,len(send_link))
    for i in range(x) :
      res = requests.get(send_link[i])
      txt = res.text
      status = res.status_code
      soup1 = BeautifulSoup(txt, 'html.parser')
      data = soup1.select('div.box-info > div')[1]
      title_data = soup1.select('div.box-info > div > h1')[0].text
      link = data.select('ul >li> a')[0].get('href')
      li2 = data.select('ul.list')[0].select('li')[3]
      li3 = data.select('ul.list')[1].select('li')[3]
      li4 = data.select('ul.list')[1].select('li')[4]
      size_data = li2.select('span')[0].text
      seed = li3.select('span')[0].text
      leech = li4.select('span')[0].text
      magnet_link.append(link)
      seeders.append(seed)
      leechers.append(leech)
      size.append(size_data)
      title.append(title_data)

    return magnet_link,seeders,leechers,size,title


