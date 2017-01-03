# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
import json
import wget
import os
import shlex
import urllib2
import re
import mysql.connector
from mysql.connector import errorcode


def upload_youtube(link,title,desc,keyword):
    os.chdir('/home/hadn/laravel')
    wget.download(link)
    file_mp4 = link.split("/")[-1]
    cmd = '/home/hadn/python/bin/python /home/hadn/hang.cucku/hang.cucku-upload-youtube.py --file "%s" --title "%s" --description "%s" --keywords "%s" --category=25' % (file_mp4, title, desc, keyword)
    cmd = shlex.split(cmd.encode('utf8'))
    print cmd
    try:
        up = Popen(cmd, stdout=PIPE)
        temp = up.communicate()
        #: remove file which uploaded to youtube
        os.remove(file_mp4)
        return temp[0].split()[-4]
    except Exception as e:
        print str(e)
        pass

def add_to_playlist(videoId):
    cmd = '/home/hadn/python/bin/python /home/hadn/hang.cucku/playlist_item.py --videoId %s' % (videoId)
    cmd = shlex.split(cmd)
    print cmd
    try:
        up = Popen(cmd, stdout=PIPE)
        temp = up.communicate()
    except Exception as e:
        print str(e)
        pass


db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='yii', use_unicode=True)
cursor = db.cursor()
sql = "select link_mp4, yt_id, id, title, description from vtv where category_id='trong-nuoc' and yt_id is NULL"
cursor.execute(sql)

for (link_mp4, yt_id, id, title, description) in cursor:
    try:
        desc = title + description
        videoId = upload_youtube(link_mp4,title,desc,'trong-nuoc')
        #print link_mp4, title
        url = 'http://backend.alobet68.com/posts/%s/%s/yt_update' % (id, videoId.split("'")[1])
        print url
        urllib2.urlopen(url)
        #print videoId
        add_to_playlist(videoId.split("'")[1])
    except Exception as e:
        print str(e)

cursor.close()
db.close()
