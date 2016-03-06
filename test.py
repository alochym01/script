from bs4 import BeautifulSoup
import urllib2
import shlex
import os
import re
import sys
import wget
import json
from subprocess import Popen, PIPE


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

print sys.argv[-1]
url = sys.argv[-1]

soup = mysoup(url)

article = soup.find("article")
print article
tags_p =[]
img = article.find('img').get('src')
print img
for p in article.find_all('p'):
    print type(p)
    tags_p.append(p)

print tags_p
with open('videos.json') as f:
    video = json.loads(f.read())
print json.dumps(video, indent=1, ensure_ascii=False)
#update video json file with img + data
video['items'][0]['snippet']['img'] = img
video['items'][0]['snippet']['data'] = []
print tags_p
for i in tags_p:
    video['items'][0]['snippet']['data'].append(unicode(i))
print json.dumps(video, indent=1, ensure_ascii=False)
with open('/home/hadn' + sys.argv[-1], 'wb') as f:
    f.write(json.dumps(video,indent=1, ensure_ascii=False).encode('utf-8'))
#print tags_p'''
