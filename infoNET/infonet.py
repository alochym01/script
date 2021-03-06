from bs4 import BeautifulSoup
import urllib2
import sys
import shlex
import os
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

current_dir = os.getcwd()
sample_file = '%s/%s' % (current_dir, 'infonet.txt')
links_from_file = read(sample_file)

link_new = []
for link in set(links):
    if link in links_from_file:
        print link
        break
    link_new.append(link)

# remove duplicate items
if len(link_new):
    save(sample_file, set(links))

for i in link_new:
    print i
    cmd = '/home/hadn/python/bin/python %s/infonet_detail.py http://infonet.vn%s' % (current_dir, i)
    print cmd
    cmd = shlex.split(cmd)
    print cmd
    try:
        up = Popen(cmd, stdout=PIPE)
        print up.communicate()
    except Exception as e:
        print str(e)
        pass

