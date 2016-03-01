from bs4 import BeautifulSoup
import urllib2
import shlex
import os
import wget
from subprocess import Popen, PIPE

def mysoup(link):
    url = urllib2.Request(link, headers={ 'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:33.0) Gecko/20100101 Firefox/33.0' })
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    return soup

#def upload_youtube(link,title,desc,keyword):
def upload_youtube(link):
    #cmd = '/home/hadn/Downloads/adsense/python/bin/python /home/hadn/Downloads/adsense/vtv_detail_v2.py %s' % link
    cmd = '/home/hadn/Downloads/adsense/vtv_detail_v2.sh %s' % link
    cmd = shlex.split(cmd.encode('utf8'))
    print cmd
    try:
        up = Popen(cmd, stdout=PIPE)
        print up.communicate()
    except Exception as e:
        print str(e)
        pass


soup = mysoup("http://vtv.vn/truyen-hinh-truc-tuyen.htm")
videos_new = soup.find("div",{"class":"video-news-box"}).find("ul",{"class":"list-item"}).find_all("li")

links = []

for video in videos_new:
    link = "http://vtv.vn"+video.find("a").get("href")
    links.append(link)

if not links:
    sys.exit(0)

with open('/home/hadn/Downloads/adsense/vtv.txt') as f:
    link_traced = f.readlines()[0].split(',')

index = 0
for link in links:
    if link in link_traced:
        break
    index += 1

if index > 0:
    with open('/home/hadn/Downloads/adsense/vtv.txt', 'w') as f:
        f.write(','.join(links[:index]))

for link in links[:index]:
    try:
        upload_youtube(link)
    except:
        pass

