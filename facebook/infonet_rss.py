# -*- coding: utf-8 -*-
import MySQLdb
import feedparser
from datetime import datetime

url = 'http://infonet.vn/Rss/Feed.aspx'
db = MySQLdb.connect("localhost", "root", "abc@123", "yii", use_unicode=True, charset="utf8")
cursor = db.cursor()

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
    try:
        img = item.links[1].href
        title = item.title
        link = item.link
        summary = item.header
        pub = item.published
        print 'image \t%s' % img
        print 'title \t%s' % title
        print 'link \t%s' % link
        print 'summary \t%s' % summary
        print 'published \t%s' % pub
        sql = "insert into alobao(link, image, title, content, pub, create_at) values ('%s', '%s', '%s', '%s', '%s', '%s')" % (link,
                                                                                                            img,
                                                                                                            title,
                                                                                                            summary,
                                                                                                            pub,
                                                                                                            str(datetime.now()))
        cursor.execute(sql)
        db.commit()
    except:
        pass
