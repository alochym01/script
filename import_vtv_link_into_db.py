# -*- coding: utf-8 -*-
import MySQLdb
from bs4 import BeautifulSoup, NavigableString
import urllib2
import re
import datetime

def mysoup(link):
    url = urllib2.Request(link, headers={ 'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:33.0) Gecko/20100101 Firefox/33.0' })
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read(), "html5lib")
    return soup

db = MySQLdb.connect("localhost", "root", "abc@123", "vtv", use_unicode=True, charset="utf8")
cursor = db.cursor()

soup = mysoup("http://vtv.vn/truyen-hinh-truc-tuyen.htm")
videos_new = soup.find("div",{"class":"video-news-box"}).find("ul",{"class":"list-item"}).find_all("li")

for j in videos_new:
    for i in j.children:
        if isinstance(i.next_element, NavigableString):
            if i.name != None:
                if i.name == 'a':
                    print i.text
                    link = i.get('href')
                if i.name == 'div' and i['class'][0] == 'sapo':
                        print i.text
                        desc = i.text

    source = 'vtv'
    category = link.split('/')[1]
    temp_link = 'http://vtv.vn%s' % link
    soup = mysoup(temp_link)
    title = re.sub('\|(.*)$', '',soup.title.text)

    sql = "select link from vtv where link='%s'"  % temp_link
    print sql
    cursor.execute(sql)
    if cursor.fetchone():
        break

    try:
        pattern_film = re.compile('=vtv/(.*).mp4')
        link_mp4 = 'http://hls.vcmedia.vn/%s' % re.search(pattern_film, str(soup)).group().replace('=vtv', 'vtv')
    except Exception as e:
        print str(e)

    tags = 'kinh-te'
    s = []
    try:
        tags = soup.find("div",{"class":"tag"}).find_all("li")
        for i in tags:
            for j in i.children:
                s.append(j.get('title'))
        tags = ','.join(s)
    except:
        pass
    sql = "insert into vtv(title, link, category_id, description, source, link_mp4,Ins, tags) value('%s', '%s', '%s', '%s', '%s', '%s',%d, '%s')" % (title, temp_link, category, desc, source, link_mp4, int(datetime.datetime.now().strftime("%Y%m%d")), tags)
    print sql
    cursor.execute(sql)
    db.commit()
