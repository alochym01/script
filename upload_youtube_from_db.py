# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
import shlex
import os
import wget
import MySQLdb
import datetime
import sys

def upload_youtube(link,title,desc,keyword):
    os.chdir('/home/hadn/Downloads/adsense/donguyenha')
    wget.download(link)
    file_mp4 = link.split("/")[-1]
    cmd = '/home/hadn/python/bin/python /home/hadn/Downloads/adsense/donguyenha-upload-youtube.py --file "%s" --title "%s" --description "%s" --keywords "%s" --category=25' % (file_mp4, title, desc, keyword)
    cmd = shlex.split(cmd.encode('utf8'))
    print cmd
    try:
        up = Popen(cmd, stdout=PIPE)
        temp = up.communicate()
        print temp
        #: remove file which uploaded to youtube
        os.remove(file_mp4)
        return temp[0].split()[-4]
    except Exception as e:
        print str(e)
        pass

def add_video_to_playlist(videoId, playlistId):
    cmd = '/home/hadn/python/bin/python /home/hadn/Downloads/adsense/donguyenha/playlist_item.py --videoId %s --playlistId %s' % (videoId, playlistId)
    cmd = shlex.split(cmd)
    print cmd
    try:
        up = Popen(cmd, stdout=PIPE)
        temp = up.communicate()
        print temp
    except Exception as e:
        print str(e)
        pass

db = MySQLdb.connect("localhost", "root", "abc@123", "vtv", use_unicode=True, charset="utf8")
cursor = db.cursor()

sql = "select * from vtv where category_id='%s' and Ins=%d" % (sys.argv[-1], int(datetime.datetime.now().strftime("%Y%m%d")))
cursor.execute(sql)

for i in cursor.fetchall():
    link = i[7]
    title = i[1]
    desc = i[5]
    keyword = i[12]
    print desc
    upload_youtube(link,title,desc,keyword)
