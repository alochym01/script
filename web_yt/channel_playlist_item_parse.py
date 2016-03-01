# -*- coding: utf8 -*-

import requests
import json
import sys

def playlist_item_parse(data):
    cmds = []
    for temp in data:
        for k, v in temp.items():
            if k == 'snippet':
                #: snippet keys [u'playlistId', u'thumbnails', u'title', u'resourceId', u'channelId', u'publishedAt', u'channelTitle', u'position', u'description']
                videoId = v['resourceId']['videoId']
                print videoId
                cmd = '/home/hadn/python/bin/python /home/hadn/youtube/script/web_yt/yt_video_detail_parse.py %s' % videoId
                cmds.append()
    return cmds


def playlist_parse(data):
    #: items keys [u'snippet', u'kind', u'etag', u'id']
    for k, v in data.items():
        if k == 'items':
            playlist_item_parse(v)


playlistId = sys.argv[1]
APIkey = 'AIzaSyB6JZxYxR9OpxIQ0wbvZD_DnJcTVt4MihU'
#: example: https://www.googleapis.com/youtube/v3/channels?part=snippet&id=UCayhFYQuenXX0ClL23kQj5A&key=AIzaSyB6JZxYxR9OpxIQ0wbvZD_DnJcTVt4MihU
url = 'https://www.googleapis.com/youtube/v3/playlistItems?maxResults=50&part=snippet&playlistId=%s&key=%s' % (playlistId, APIkey)

print url
rv = requests.get(url)

playlist_parse(rv.json())
