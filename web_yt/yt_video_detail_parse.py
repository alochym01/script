import requests
import sys
import json

def video_parse_detail(data):
    for i in data:
        v_id = i['id']
        v_kind = i['kind']
        v_statistics = i['statistics']
        v_etag = i['etag']
        v_snippet_thumbnails = i['snippet']['thumbnails']
        v_snippet_title = i['snippet']['title']
        v_snippet_localized = i['snippet']['localized']
        v_snippet_channelId = i['snippet']['channelId']
        v_snippet_publishedAt = i['snippet']['publishedAt']
        v_snippet_liveBroadcastContent = i['snippet']['liveBroadcastContent']
        v_snippet_channelTitle = i['snippet']['channelTitle']
        v_snippet_categoryId = i['snippet']['categoryId']
        v_snippet_description = i['snippet']['description']
        v_snippet_tags = i['snippet']['tags']
        print v_id
        print v_kind
        print v_statistics
        print v_etag
        print v_snippet_thumbnails
        print v_snippet_title
        print v_snippet_localized
        print v_snippet_channelId
        print v_snippet_publishedAt
        print v_snippet_liveBroadcastContent
        print v_snippet_channelTitle
        print v_snippet_categoryId
        print v_snippet_description
        print v_snippet_tags


key =  'AIzaSyB6JZxYxR9OpxIQ0wbvZD_DnJcTVt4MihU'
url = 'https://www.googleapis.com/youtube/v3/videos?id=%s&key=%s&part=snippet,statistics' % ('tfch-HgmqpI', key)
print url

data = requests.get(url)

ata = data.json()

kind = ata['kind']
etag = ata['etag']
pageInfo = ata['pageInfo']
items = ata['items']

video_parse_detail(items)
print json.dumps(ata)
