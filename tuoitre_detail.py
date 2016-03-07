from bs4 import BeautifulSoup
import urllib2
import json
import sys
import wget
import os


def mysoup(link):
    url = urllib2.Request(link, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:33.0) Gecko/20100101 Firefox/33.0'})
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read(), "html5lib")
    return soup

url = sys.argv[-1].split('\n')[0]

soup = mysoup(url)

print url
soup = mysoup(url)

section = soup.find('section', {'class': 'content'})
try:
    tbody = section.find('tbody')
    img = tbody.find('img').get('src')
except Exception as e:
    print str(e)
    pass
tags_p = []

for p in section.find_all('p'):
    tags_p.append(p)

# remove unuse content
for i in range(5):
    del tags_p[-1]

with open('videos.json') as f:
    video = json.loads(f.read())

try:
    video['items'][0]['snippet']['url'] = url
    video['items'][0]['snippet']['img'] = img
except:
    video['items'][0]['snippet']['img'] = ''

video['items'][0]['snippet']['data'] = []
for i in tags_p:
    video['items'][0]['snippet']['description'] += unicode(i)

folder_path = '%s/tuoitre/%s' % (os.getcwd(), url.split('/')[-1].split('.')[0])
os.mkdir(folder_path)

with open(folder_path + '/' + url.split('/')[-1], 'wb') as f:
    f.write(json.dumps(video, indent=1, ensure_ascii=False).encode('utf-8'))

try:
    os.getcwd()
    os.chdir(folder_path)
    wget.download(img)
except Exception as e:
    print str(e)
