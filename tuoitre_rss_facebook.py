# -*- coding: utf-8 -*-
from __future__ import division
import MySQLdb
import feedparser
import re
from datetime import datetime
from subprocess import Popen, PIPE
import shlex
import urllib
import facebook
import imageio

pattern = re.compile('src="(.*).jpg"')

url = 'http://tuoitre.vn/rss/tt-tin-moi-nhat.rss'
db = MySQLdb.connect("localhost", "root", "abc@123", "yii", use_unicode=True, charset="utf8")
cursor = db.cursor()

img_path = '/home/hadn/Downloads'
img_path_edit = '/home/hadn/Downloads/scripts'
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
        img = pattern.search(item.summary).group().split('=')[1]
        img = re.sub('"', '', img)
        img = re.sub('/s146/', '/s626/', img)
        temp_path = '%s/%s' % (img_path, img.split('/')[-1])
        img_path_ffmpeg = '%s/%s' % (img_path_edit, img.split('/')[-1])
        # download img from website and save as temp_path
        urllib.urlretrieve(img, temp_path)
        im = imageio.imread(temp_path)
        img_h, img_w, img_v = im.shape
        if img_w/img_h > 1.3:
            value = img_h*4/3
            value_crop = img_w - value
            cmd = '/usr/bin/ffmpeg -i %s -vf "crop=%s:ih:%s/2:ih/2" %s -y' % (temp_path, value, value_crop, img_path_ffmpeg)
            print cmd
        else:
            value = img_w*3/4
            value_crop = img_h - value
            cmd = '/usr/bin/ffmpeg -i %s -vf "crop=iw:%s:iw/2:%s/2" %s -y' % (temp_path, value, value_crop, img_path_ffmpeg)
            print cmd
        cmd = shlex.split(cmd)
        print cmd
        process = Popen(cmd, stdout=PIPE)
        process.wait()
        cmd_normalize_640 = '/usr/bin/ffmpeg -i %s -vf scale=640:-1 %s -y' % (img_path_ffmpeg, temp_path)
        cmd_normalize_640 = shlex.split(cmd_normalize_640)
        print cmd_normalize_640
        process = Popen(cmd_normalize_640, stdout=PIPE)
        process.wait()
        title = item.title
        # upload img to facebook
        photo = graph.put_photo(image=open(temp_path, 'rb'),  message=title)
        photoid = '%s?fields=images' % photo['id']
        img_temp = graph.get_object(id=photoid)
        for i in img_temp['images']:
            source, width, height = i.items()
            print height
            if  height[-1] == 130:
                img_link = source[-1]
                print img_link
            if  height[-1] > 400:
                img_big = source[-1]
                print img_big
        link = item.link
        summary = item.summary
        pub = item.published
        sql = "insert into alobao(link, image, title, content, pub, image_big, create_at) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (link,
                                                                                                            img_link,
                                                                                                            title,
                                                                                                            summary,
                                                                                                            pub,
                                                                                                            img_big,
                                                                                                            str(datetime.now()))
        print sql
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print link
        print str(e)
        pass
