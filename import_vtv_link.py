import re
import os, sys
import MySQLdb
import datetime
import urllib2
from bs4 import BeautifulSoup, NavigableString
import sys

def mysoup(link):
    url = urllib2.Request(link, headers={ 'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:33.0) Gecko/20100101 Firefox/33.0' })
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read(), "html5lib")
    return soup

db = MySQLdb.connect("localhost", "root", "abc@123", "vtv", use_unicode=True, charset="utf8")
cursor = db.cursor()

source = 'vtv'

#path = '/home/hadn/Downloads/adsense/vtv_link_save/'
#dirs = os.listdir(path)
#for file in dirs:
#    f = '%s%s' % (path,file)
#    print f
with open(sys.argv[-1]) as temp:
    for i1 in temp:
        category = i1.split('/')[3]
        print category
        print i1
        try:
            soup = mysoup(i1)
            title = re.sub("'|\|(.*)$", '',soup.title.text)
            print title
        except:
            pass

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
            print tags
        except:
            pass

        sql = "insert into vtv(title, link, category_id, source, link_mp4,Ins, tags) value('%s', '%s', '%s', '%s', '%s',%d, '%s')" % (title, i1, category, source, link_mp4, int(datetime.datetime.now().strftime("%Y%m%d")), tags)
        print sql
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print str(e)
            pass
