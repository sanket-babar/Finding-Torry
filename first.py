import requests
from bs4 import BeautifulSoup
res = requests.get(
    'https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')
txt = res.text
status = res.status_code

soup = BeautifulSoup(txt, 'html.parser')

page_title = soup.title.string

print(page_title)