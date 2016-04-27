# -*- coding: utf-8 -*-
import MySQLdb
import feedparser
from datetime import datetime

import urllib
import facebook

url = 'http://infonet.vn/Rss/Feed.aspx'
db = MySQLdb.connect("localhost", "root", "abc@123", "yii", use_unicode=True, charset="utf8")
cursor = db.cursor()

img_path = '/home/hadn/Downloads'
fb_token_key = 'CAAKZB8aoNPK8BAEZCTWZBVURUt485NSyzZBLMmUxzrkNd4UbI7EJdGcXJgJqJDtZCj6qRTjpGH23NAlK31TZC63hWDDA5L0K7VZCDU2XU11HLX6EEaZBQvlHcMe9poDSNAEjevhquu18TcrRZAFVWBZBHAiobEjTBgamTuG94d0CkbXXO7SWW9xYOt'
graph = facebook.GraphAPI(access_token=fb_token_key)

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
        temp_path = '%s/%s' % (img_path, img.split('/')[-1])
        urllib.urlretrieve(img, temp_path)
        title = item.title
        photo = graph.put_photo(image=open(temp_path, 'rb'),  message=title)
        photoid = '%s?fields=images' % photo['id']
        img_temp = graph.get_object(id=photoid)
        for i in img_temp['images']:
            source, width, height = i.items()
            #print i.items()
            print height
            if  height[-1] == 130:
                img_link = source[-1]
                print img_link
                break
        link = item.link
        summary = item.header
        pub = item.published
        #print 'image \t%s' % img
        #print 'image \t%s' % img_temp
        #print 'title \t%s' % title
        #print 'link \t%s' % link
        #print 'summary \t%s' % summary
        #print 'published \t%s' % pub
        sql = "insert into alobao(link, image, title, content, pub, create_at) values ('%s', '%s', '%s', '%s', '%s', '%s')" % (link,
                                                                                                            img_link,
                                                                                                            title,
                                                                                                            summary,
                                                                                                            pub,
                                                                                                            str(datetime.now()))
        #print sql
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print str(e)
        pass
