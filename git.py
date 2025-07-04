from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests

import re

file2 = open("git.txt", "a")

# https://github.com/search?p=' + str(x + 1) + '&q=stackoverflow&ref=simplesearch&type=Repositories
# https://github.com/search?l=JavaScript&p=' + str(x + 1) + '&q=stackoverflow&type=Repositories

# JavaScript, 

for x in range(10):
    url = Request('https://github.com/search?l=JavaScript&p=' + str(x + 1) + '&q=stackoverflow&type=Repositories', headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    linktext = ""
    links = soup.find_all('a', {'class' : 'v-align-middle'})
    for link in links:
        linktext += "https://github.com" + link['href'] + "\n"
    file2.write(linktext)

print("end")
file2.close()
