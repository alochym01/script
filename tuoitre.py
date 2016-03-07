from bs4 import BeautifulSoup
import urllib2
import re
import json
import sys
import shlex
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

div = soup.find('div', {'class':'newhot_most_content'})

#crawler all links in tuoitre category
links = []
for i in set(div.find_all('a')):
    try:
        links.append(i.get('href'))
    except:
        pass
# ==========end===========

#begin to compare a links value(info_net.txt) with links temp value(info_net_temp)
links_from_file = read('info_net.txt')

link_new = []
for link in set(links):
    if link in links_from_file:
        print link
        break
    link_new.append(link)

#remove duplicate items
if len(link_new):
    save('info_net.txt', set(links))

for i in link_new:
    print i
    cmd = '/home/hadn/python/bin/python /home/hadn/script/tuoitre_detail.py %s' % i
    print cmd
    cmd = shlex.split(cmd)
    print cmd
    try:
        up = Popen(cmd, stdout=PIPE)
        print up.communicate()
    except Exception as e:
        print str(e)
        pass
