# -*- coding: utf8 -*-
import requests
import json
import sys
import urllib2

#: how to crawl all videos of channel
#: python crawler_yt_playlist_rest.py channelID catID
#: need 2 variables:
#:  1.  channelId - store in file channel_ID.txt
#:  2.  API key from google console - store in file api_public_key.txt
#                "description" : json.dumps(data["description"]),
#for i in items:
#    temp = channelDetails(i["snippet"])

def channelDetails(data):
    temp = {
                "thumbnails_json" : json.dumps(data["thumbnails"]),
                "title" : data["title"],
                "youtubeChannelId" : data["channelId"],
                "description" : data["description"],
                "streamUrl" : "https://www.youtube.com/watch?v=%s" % data["resourceId"]["videoId"],
                "youtubeId" : data["resourceId"]["videoId"],
                "catId" : int(sys.argv[-1])
            }
    print data["title"]
    return temp

with open('/home/hadn/youtube/script/api_public_key.txt') as f:
    APIkey = f.read().strip()

print sys.argv[1]
print sys.argv[-1]
playlistId = sys.argv[-2]

url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=%s&key=%s' % (playlistId, APIkey)
print url
<<<<<<< HEAD
url_api = "http://localhost/rest/by-yt-id"
=======
#url_api = "http://localhost:81/rest/by-yt-id"
>>>>>>> d5e067f49fdb382e1f58f5c6ad687084a3778f33
url_api = "http://rest.alobet68.com/rest/by-yt-id"
while True:
    rv = requests.get(url)
    temp_rv = rv.json()
    items = temp_rv['items']
    for i in items:
        temp = channelDetails(i["snippet"])
<<<<<<< HEAD
        print json.dumps(temp, indent=2)
        try:
            rv = requests.put(url_api, data=temp)
            print rv.url
        except Exception, e:
            print str(e)
            pass
    print temp_rv.keys()
    nextPageToken = temp_rv["nextPageToken"]
    #nextPageToken = str(rv.json()['nextPageToken'])
=======
        #try:
        rest = requests.put(url_api, data=temp)
        print rest.url
        #except Exception, e:
        #    print str(e)
        #    pass
    nextPageToken = str(rv.json()['nextPageToken'])
>>>>>>> d5e067f49fdb382e1f58f5c6ad687084a3778f33
    url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=%s&key=%s&pageToken=%s' % (playlistId, APIkey, nextPageToken)
    print nextPageToken
    print url
