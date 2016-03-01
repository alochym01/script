# -*- coding: utf8 -*-
import requests
import json
import sys


#: how to crawl all videos of channel
#: need 2 variables:
#:  1.  VideoId - get from sys.argv
#:  2.  CatID of video - get from sys.argv
#:  3.  API key from google console - store in file api_public_key.txt
#                "description" : json.dumps(data["description"]),
#:  4.  example: python crawler_yt_videoId_rest.py videoID CatID

with open('/home/hadn/youtube/script/api_public_key.txt') as f:
    APIkey = f.read().strip()

videoId = sys.argv[-2]

url = 'https://www.googleapis.com/youtube/v3/videos?id=%s&key=%s&part=snippet,contentDetails' % (videoId, APIkey)
print url
url_api = "http://localhost/rest/by-yt-id"

rv = requests.get(url)
items = rv.json()['items']
try:
    temp = {
        "thumbnails_json" : items[0]["snippet"]["thumbnails"],
        "title" : items[0]["snippet"]["title"],
        "youtubeChannelId" : items[0]["snippet"]["channelId"],
        "description" : items[0]["snippet"]["description"],
        "streamUrl" : "https://www.youtube.com/watch?v=%s" % sys.argv[-2],
        "youtubeId" : sys.argv[-2],
        "catId" : int(sys.argv[-1])
    }
    rv = requests.put(url_api, data=temp)
    print rv.text
except Exception, e:
    print str(e)
    pass
