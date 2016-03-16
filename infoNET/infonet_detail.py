"""
    line 45: tags_p should be article.find_all('div')
    http://infonet.vn/: - description ->  tags_div
        suc-khoe/14.info
    http://infonet.vn/: - description ->  tags_p
        kinh-doanh/4.info
        giao-duc/1064.info
        huong-nghiep/1145.info
        quan-su/58.info
"""
from bs4 import BeautifulSoup
import urllib2
import wget
import json
import sys
import os
from string import letters, digits
import random
import re


def mysoup(link):
    url = urllib2.Request(link, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:33.0) Gecko/20100101 Firefox/33.0'})
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

current_dir = os.getcwd()
folder_name = ''.join(random.choice(letters + digits) for _ in range(11))
folder_path = '%s/infonet/%s' % (current_dir, folder_name)
sample_file = '%s/%s' % (current_dir, 'videos.json')
slug = url.split('/')

soup = mysoup(url)

article = soup.find("article")
title = re.sub('\n|\t', '', soup.title.text.split(' | ')[0])
tags_div = []

for p in article.find_all('p'):
    tags_div.append(p)

with open(sample_file) as f:
        video = json.loads(f.read())

# update video json file with img + data
os.mkdir(folder_path)

try:
    os.chdir(folder_path)
    img = article.find('img').get('src')
    wget.download(img)
    video['items'][0]['snippet']['url'] = url
    video['items'][0]['snippet']['img'] = img
    video['items'][0]['etag'] = slug[-1].split('post')[0]
    if img != '':
        video['items'][0]['snippet']['thumbnails']['default']['url'] = slug[-1].split('post')[0] + 'small.jpg'
        video['items'][0]['snippet']['thumbnails']['standard']['url'] = slug[-1].split('post')[0] + 'standard.jpg'
except Exception as e:
    print str(e)

video['items'][0]['snippet']['data'] = []
video['items'][0]['snippet']['description'] += title
video['items'][0]['snippet']['title'] = title
for i in tags_div:
    video['items'][0]['snippet']['description'] += unicode(i)

filename = '%s/%s.json' % (folder_path, folder_name)
with open(filename, 'wb') as f:
    f.write(json.dumps(video, indent=1, ensure_ascii=False).encode('utf-8'))
