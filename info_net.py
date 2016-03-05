from bs4 import BeautifulSoup
import urllib2
import shlex
import os
import re
import wget
from subprocess import Popen, PIPE

def mysoup(link):
    url = urllib2.Request(link, headers={ 'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:33.0) Gecko/20100101 Firefox/33.0'  })
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read(), "html5lib")
    return soup

url = 'http://infonet.vn/kinh-doanh/4.info'

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
#remove duplicate items
#print list(set(links))


#save temp value into tem file
with open('info_net_temp.txt', 'w') as f:
    f.write(','.join(set(links)))



#begin to compare a links value(info_net.txt) with links temp value(info_net_temp)
with open('info_net.txt') as f:
    try:
        links_from_file = f.read().split(',')
    except:
        links_from_file = []
        pass

with open('info_net_temp.txt') as f:
    try:
        links_temp = f.read().split(',')
    except:
        links_temp = []
        pass

if len(list(set(links_temp) - set(links_from_file))):
    print list(set(links_temp) - set(links_from_file))
    with open('info_net.txt', 'w') as f:
        f.write(','.join(set(links)))

