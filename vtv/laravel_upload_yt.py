# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
import json
import wget
import os
import shlex
import urllib2
import re

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

path = '/mnt/html_css3/chym/storage/app/'
dirs = os.listdir(path)
for file in dirs:
    try:
        f = '%s%s' % (path, file)
        with open(f) as f:
            temp = json.loads(f.read())

        link_mp4 = temp['link_mp4']
        title = re.sub('"', '', temp['title'])
        desc = '%s %s' % (title, re.sub('"', '', temp['description']))
        keyw = temp['tags']
        videoId = upload_youtube(link_mp4,title,desc,keyw)
        # remove file in laravel folder
        url = 'http://backend.alobet68.com/posts/%s/%s/yt_update' % (temp['id'], videoId.split("'")[1])
        #print url
        urllib2.urlopen(url)
        #print videoId
        add_to_playlist(videoId.split("'")[1])
    except Exception as e:
        #print str(e)
        pass
