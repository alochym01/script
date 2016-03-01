# -*- coding: utf8 -*-

import requests
import json
import sys

#: use python file_name channel_id(UCayhFYQuenXX0ClL23kQj5A)
#: get playlist ID ==> channelId
#: the name of playlist ==> title
def channel_item_parse(data):
    for i in data:
        channelId = i['snippet']['channelId']
        title = i['snippet']['title']
        print 'channel ID \t:%s' % channelId
        print 'title \t:%s' % title

def channel_parse(data):
    kind = data['kind']
    etag = data['etag']
    pageInfo = data['pageInfo']
    items = data['items']
    print kind
    print etag
    print pageInfo
    channel_item_parse(items)

channelId = sys.argv[1]
APIkey = 'AIzaSyB6JZxYxR9OpxIQ0wbvZD_DnJcTVt4MihU'
#: example: # https://www.googleapis.com/youtube/v3/playlists?part=snippet&maxResults=50&channelId=UCtuI-seWsvKPb8MxkqY-fDw&key=AIzaSyB6JZxYxR9OpxIQ0wbvZD_DnJcTVt4MihU
url = 'https://www.googleapis.com/youtube/v3/playlists?maxResults=50&part=snippet&channelId=%s&key=%s' % (channelId, APIkey)

rv = requests.get(url)

channel_parse(rv.json())
