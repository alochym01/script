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
# check if img != '':
#   thumbnails['default']['url'] has value
#   thumbnails['standard']['url'] has value
img = ''
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

current_dir = os.getcwd()
sample_file = '%s/%s' % (current_dir, 'videos.json')
slug = url.split('/')
folder_path = '%s/tuoitre/%s' % (current_dir, slug[-1].split('.')[0])

with open(sample_file) as f:
    video = json.loads(f.read())

try:
    video['items'][0]['snippet']['url'] = url
    video['items'][0]['snippet']['img'] = img
except:
    video['items'][0]['snippet']['img'] = ''

video['items'][0]['snippet']['data'] = []
video['items'][0]['snippet']['description'] += unicode(soup.title.text)
for i in tags_p:
    video['items'][0]['snippet']['description'] += unicode(i)

os.mkdir(folder_path)

try:
    os.chdir(folder_path)
    wget.download(img)
    video['items'][0]['etag'] = slug[-2]
    if img != '':
        video['items'][0]['snippet']['thumbnails']['default']['url'] = slug[-2] + '-small.jpg'
        video['items'][0]['snippet']['thumbnails']['standard']['url'] = slug[-2] + '-standard.jpg'
except Exception as e:
    print str(e)

with open(folder_path + '/' + slug[-1], 'wb') as f:
    f.write(json.dumps(video, indent=1, ensure_ascii=False).encode('utf-8'))
