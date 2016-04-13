# -*- coding: utf-8 -*-
import MySQLdb
import feedparser
import re
from datetime import datetime

pattern = re.compile('src="(.*).jpg"')

db = MySQLdb.connect("localhost", "root", "abc@123", "yii", use_unicode=True, charset="utf8")
cursor = db.cursor()

sql = 'insert into alobao(link, image, title, content, pub) values ()'
url = 'http://tuoitre.vn/rss/tt-tin-moi-nhat.rss'

feed = feedparser.parse(url)
# keys = ['feed',
#        'status',
#        'version',
#        'encoding',
#        'bozo',
#        'headers',
#        'href',
#        'namespaces',
#        'entries',
#        'bozo_exception']

for item in feed['entries']:
    img = pattern.search(item.summary).group().split('=')[1]
    title = item.title
    link = item.link
    summary = item.summary
    pub = item.published
    print 'image \t%s' % img
    print 'title \t%s' % title
    print 'link \t%s' % link
    print 'summary \t%s' % summary
    print 'published \t%s' % pub
    print '==========================='
    sql = "insert into alobao(link, image, title, content, pub, create_at) values ('%s', %s, '%s', '%s', '%s', '%s')" % (link,
                                                                                                          img,
                                                                                                          title,
                                                                                                          summary,
                                                                                                          pub,
                                                                                                                         str(datetime.now()))
    cursor.execute(sql)
    db.commit()
