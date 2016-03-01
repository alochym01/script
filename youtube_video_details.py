# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup, NavigableString
import json
import re
import sys
from subprocess import Popen, PIPE
import shlex
import os
import requests

def xml_parse(entry, updatevideoId):
    videoId = entry.id.get_text().split(':')[-1].encode("utf-8")
    title = entry.title.get_text().encode("utf-8")
    link = entry.link['href'].encode("utf-8")
    updated = entry.updated.get_text().encode("utf-8")
    if videoId == updatevideoId:
        return {
                    "videoId" : videoId,
                    "title" : title,
                    "link" : link,
                    "updated" : updated,
                    "description" : "",
                    "is_new" : 0
                }
    return {
                "videoId" : videoId,
                "title" : title,
                "link" : link,
                "updated" : updated,
                "description" : "",
                "is_new" : 1
            }

def VideoDetails(videoId):
    payload_videoId = {
        'id' : videoId,
        'key' : 'AIzaSyB6JZxYxR9OpxIQ0wbvZD_DnJcTVt4MihU',
        'part' : 'snippet,statistics'
    }
    channel_url = 'https://www.googleapis.com/youtube/v3/videos'
    data = requests.get(channel_url, params=payload_videoId)
    video = data.json()['items'][0]
    print "View Count %s" % video['statistics']['viewCount']
    print "Title %s" % video['snippet']['title']
    print "Description %s" % video['snippet']['description']
    print "Category %s" % video['snippet']['categoryId']
    print "Thumbnails %s" % video['snippet']['thumbnails']
    print video
    #playlist_id = data.json()['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    #return playlist_id
url = 'http://www.youtube.com/feeds/videos.xml?channel_id=%s' % sys.argv[-1]
print url
proxies={'http': 'http://210.245.31.7:80'}
data = requests.post(url, proxies=proxies)

soup = BeautifulSoup(data.content)
file = '/dev/shm/channel_%s.txt' % sys.argv[-1]
with open(file) as f:
    #: get update time from channel
    #: if updatevideoId is NONE, set updatevideoId = {"videoId" : "1234"}
    try:
        #data = re.sub("'", '"',f.read())
        #updatevideoId = json.loads(data)
        updatevideoId = f.read().strip()
        print "updatevideoId============%s" % updatevideoId
    except Exception, e:
        print "error"
        updatevideoId = {"videoId" : "1234"}
        pass

news = []
try:
    #for entry in soup.html.body.feed.link.next_siblings:
    for entry in soup.feed.link.next_siblings:
        if not isinstance(entry, NavigableString) and entry.name == "entry":
            #: the return value should has rv['is_new'] = 1
            #: condition match - added the rv into news list
            rv = xml_parse(entry, updatevideoId)
            #print json.dumps(rv, indent=2)
            if rv['is_new'] == 1:
                news.append(rv)
            else:
                 break
except Exception, e:
    print str(e)
    pass

if len(news) > 0:
    #: check news has any items
    with open(file, 'w') as f:
        f.write(news[0]['videoId'])

if len(news) > 0:
    for value in news:
        VideoDetails(value['videoId'])

