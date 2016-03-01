# -*- coding: utf8 -*-

import requests
import json
import sys

def channel_item_parse(data):
    for i in data:
        kind = i['kind']
        etag = i['etag']
        id = i['id']
        thumbnails = i['snippet']['thumbnails']
        title = i['snippet']['title']
        country = i['snippet']['country']
        publishedAt = i['snippet']['publishedAt']
        localized = i['snippet']['localized']
        description = i['snippet']['description']
        print kind
        print etag
        print id
        print publishedAt
        print title
        print country
        print description
        print localized
        print thumbnails

def channel_parse(data):
    #items, kind, etag, pageInfo = data.items()
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
#: example: https://www.googleapis.com/youtube/v3/channels?part=snippet&id=UCayhFYQuenXX0ClL23kQj5A&key=AIzaSyB6JZxYxR9OpxIQ0wbvZD_DnJcTVt4MihU
url = 'https://www.googleapis.com/youtube/v3/channels?part=snippet&id=%s&key=%s' % (channelId, APIkey)

rv = requests.get(url)

channel_parse(rv.json())
