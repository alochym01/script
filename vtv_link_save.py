from bs4 import BeautifulSoup
import urllib2
import re

def mysoup(link):
     url = urllib2.Request(link, headers={ 'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:33.0) Gecko/20100101 Firefox/33.0' })
     page = urllib2.urlopen(url)
     soup = BeautifulSoup(page.read(), "html5lib")
     return soup


soup = mysoup("http://vtv.vn/truyen-hinh-truc-tuyen.htm")
videos_new = soup.find("div",{"class":"video-news-box"}).find("ul",{"class":"list-item"}).find_all("li")

with open('/home/hadn/Downloads/adsense/vtv_link_save.txt') as f:
    links = f.readlines()

with open('/home/hadn/Downloads/adsense/vtv_link_save.txt', 'a') as f:
    for video in videos_new:
        link = "http://vtv.vn" + video.find("a").get("href") + '\n'
        if not link in links:
            print link
            f.write(link)
