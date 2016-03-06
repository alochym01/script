from bs4 import BeautifulSoup
import urllib2
import re
import json
import sys

def mysoup(link):
    url = urllib2.Request(link, headers={ 'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:33.0) Gecko/20100101 Firefox/33.0'  })
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read(), "html5lib")
    return soup

def save(filename, data):
    with open(filename, 'w') as f:
        f.write(','.join(set(data)))

def read(filename):
    with open(filename) as f:
        data = f.read().split(',')
    return data

url = sys.argv[-1]

soup = mysoup(url)

div = soup.find('div', {'class':'newhot_most_content'})

#crawler all links in tuoitre category
links = []
for i in set(div.find_all('a')):
    try:
        links.append(i.get('href'))
    except:
        pass
# ==========end===========

#save temp value into tem file
save('info_net_temp.txt', set(links))

#begin to compare a links value(info_net.txt) with links temp value(info_net_temp)
links_from_file = read('info_net.txt')

links_temp = read('info_net_temp.txt')

#remove duplicate items
if len(set(links_temp) - set(links_from_file)):
    save('info_net.txt', set(links))

#begin crawler content of link
for url in list(set(links_temp) - set(links_from_file)):
    print url
    soup = mysoup(url)

    div_detail = soup.find('div', {'class':'left-side'})
    tags_p =[]

    for p in div_detail.find_all('p'):
        tags_p.append(p)
    #remove unuse content
    for i in range(5):
        del tags_p[-1]

    with open('videos.json') as f:
        video = json.loads(f.read())
    #update video json file with img + data
    try:
        video['items'][0]['snippet']['url'] = url
        img = div_detail.find_all('img')[-2].get('src')
        video['items'][0]['snippet']['img'] = img
    except:
        video['items'][0]['snippet']['img'] = ''

    video['items'][0]['snippet']['data'] = []
    for i in tags_p:
        video['items'][0]['snippet']['data'].append(unicode(i))
    with open('/home/hadn/' + url.split('/')[-1], 'wb') as f:
        f.write(json.dumps(video,indent=1, ensure_ascii=False).encode('utf-8'))
