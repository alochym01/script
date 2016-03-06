from bs4 import BeautifulSoup
import urllib2
import shlex
import os
import re
import wget
import json
from subprocess import Popen, PIPE
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

section = soup.find("section", {"class":"storylisting"})

wrap = section.find('div', {'class':'wrap'})

links = []
for i in wrap.find_all('a'):
    try:
        if i.get('href').count('/') == 1:
            links.append(i.get('href'))
    except:
        pass

#save temp value into tem file
save('info_net_temp.txt', links)

#begin to compare a links value(info_net.txt) with links temp value(info_net_temp)
links_from_file = read('info_net.txt')

links_temp = read('info_net_temp.txt')

#remove duplicate items
if len(list(set(links_temp) - set(links_from_file))):
    save('info_net.txt', links)

#begin crawler content of link
for url in list(set(links_temp) - set(links_from_file)):
    print url
    soup = mysoup('http://infonet.vn/' + url)

    article = soup.find("article")
    tags_p =[]

    for p in article.find_all('p'):
        tags_p.append(p)

    with open('videos.json') as f:
        video = json.loads(f.read())
    #update video json file with img + data
    try:
        video['items'][0]['snippet']['url'] = url
        img = article.find('img').get('src')
        video['items'][0]['snippet']['img'] = img
    except:
        video['items'][0]['snippet']['img'] = ''

    video['items'][0]['snippet']['data'] = []
    for i in tags_p:
        video['items'][0]['snippet']['data'].append(unicode(i))
    with open('/home/hadn' + url, 'wb') as f:
        f.write(json.dumps(video,indent=1, ensure_ascii=False).encode('utf-8'))
