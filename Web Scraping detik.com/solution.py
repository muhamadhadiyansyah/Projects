#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
import requests
import json
url = 'https://www.detik.com/search/searchall?query=bitcoin&sortby=time&page=%d'
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')
article = soup.find('article')
for i in range(1, 171):
    url = 'https://www.detik.com/search/searchall?query=bitcoin&sortby=time&page=%d' + str(i)
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    article = soup.find('article')
    for article in soup.find_all('article'):
        title = article.h2.text
        url = article.find('a')
        url = url['href']
        tanggal = ' '.join(article.find('span', 'date').text.split(' ')[1:])
        a = {'title':title,
             'url':url,
             'tanggal':tanggal}
        json.dump(a, open('solution.json', 'w'), indent=2)
        dataset = open("solution.json", "r")
        data = dataset.read()
        print(data)
        dataset.close()

