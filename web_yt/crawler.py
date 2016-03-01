# -*- coding: utf8 -*-
import requests
import MySQLdb
import json
import sys
import re


#: how to crawl all videos of channel
#: need 2 variables:
#:  1.  channelId - store in file channel_ID.txt
#:  2.  API key from google console - store in file api_public_key.txt

def channelDetails(data):
    '''
        sample data:
        {
          "snippet": {
            "playlistId": "UU3djj8jS0370cu_ghKs_Ong",
            "thumbnails": {
              "default": {
                "url": "https://i.ytimg.com/vi/g4TpDfmxZeg/default.jpg",
                "width": 120,
                "height": 90
              },
              "high": {
                "url": "https://i.ytimg.com/vi/g4TpDfmxZeg/hqdefault.jpg",
                "width": 480,
                "height": 360
              },
              "medium": {
                "url": "https://i.ytimg.com/vi/g4TpDfmxZeg/mqdefault.jpg",
                "width": 320,
                "height": 180
              },
              "maxres": {
                "url": "https://i.ytimg.com/vi/g4TpDfmxZeg/maxresdefault.jpg",
                "width": 1280,
                "height": 720
              },
              "standard": {
                "url": "https://i.ytimg.com/vi/g4TpDfmxZeg/sddefault.jpg",
                "width": 640,
                "height": 480
              }
            },
            "title": "ABC Song For Children by Hooplakidz",
            "resourceId": {
              "kind": "youtube#video",
              "videoId": "g4TpDfmxZeg"
            },
            "channelId": "UC3djj8jS0370cu_ghKs_Ong",
            "publishedAt": "2015-07-20T12:17:40.000Z",
            "channelTitle": "HooplaKidz",
            "position": 3,
            "description": "Come and sing along to this Brand New ABC Song to teach the alphabets to all you children !! With the tune of Humpty Dumpty nursery rhyme, kids can learn the ABC Alphabet Song in English in a easy and fun way!\n\nHope you enjoyed this new ABC Song on HooplaKidz\nFor more preschool & phonics songs, click here http://www.youtube.com/user/hooplakidz\n\nBe a part of the HooplaKidz family, click below to subscribe to our channel for regular videos! \nhttp://bit.ly/HooplaKidzSubscribe\n\n+ Visit Our Official YouTube Channel! http://www.youtube.com/hooplakidz\n+ Visit our official website! http://www.hooplakidz.com\n+ Follow us on Google Plus! http://bit.ly/hooplakidzgoogleplus\n+ Like our Facebook Fan Page http://bit.ly/HooplaKidzFacebook\n+ Check out our Pinterest Board http://bit.ly/HooplaKidzPinterest\n\nMany thanks to all our HooplaKidz fans for appreciating our videos! \n\nWe would love to hear from you so please do leave your comments and share our videos with your loved ones!\n\nYoBoHo New Media Pvt. Ltd. \u00a9 2015. All rights reserved."
          },
          "kind": "youtube#playlistItem",
          "etag": "\"iDqJ1j7zKs4x3o3ZsFlBOwgWAHU/ajUrnF7ZINf4M6qY6JDqS0Wws9o\"",
          "id": "UUCKUM8Hm5dM5OOGUHGO8zeYA_zQpbkX65"
        }
            '''
    temp = {
                "thumbnails" : data["thumbnails"],
                "title" : data["title"],
                "publishedAt" : data["publishedAt"],
                "channelId" : data["channelId"],
                "description" : json.dumps(data["description"]),
                "videoId" : data["resourceId"]["videoId"],
                "youtubeId" : data["resourceId"]["videoId"],
            }
    return temp



APIkey ='AIzaSyB6JZxYxR9OpxIQ0wbvZD_DnJcTVt4MihU'
url = 'https://www.googleapis.com/youtube/v3/playlists?maxResults=50&part=snippet&channelId=%s&key=%s' % (sys.argv[-1], APIkey)

#: sql config
#: username: root
#: password: abc@123

db = MySQLdb.connect(host="localhost",user="root", passwd="abc@123",db="yii2basic", use_unicode=True, charset='utf8')
cursor = db.cursor()

rv = requests.get(url)
for item in rv.json()['items']:
    playlistId = item['id']
    title = item['snippet']['title']
    thumbnails = item['snippet']['thumbnails']['medium']
    playlist_cmd = 'insert into yt_playlist(title, playlistid, thumbnails) value("%s", "%s", "%s")' % (re.sub("'", '', title), playlistId, thumbnails)
    cursor.execute(playlist_cmd)
    db.commit()
    url = 'https://www.googleapis.com/youtube/v3/playlistItems?maxResults=50&part=snippet&playlistId=%s&key=%s' % (playlistId, APIkey)
    while True:
        rv = requests.get(url)
        items = rv.json()['items']
        for i in items:
            videoId = i['snippet']['resourceId']['videoId']
            video_url = 'https://www.googleapis.com/youtube/v3/videos?id=%s&key=%s&part=snippet,statistics' % (videoId, APIkey)
            rv_video = requests.get(video_url)
            for j in rv_video.json()['items']:
                desc = re.sub("'", '', j['snippet']['description'])
                title = re.sub("'", '', j['snippet']['title'])
                #desc, like are the keywords of MySQL and should be escape by "`"
                video_cmd = 'insert into yt_video(title, video_id, `desc`, view, `like`, publishedAt, playlistid) value(\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' % (title, videoId, desc, j['statistics']['viewCount'], j['statistics']['likeCount'], j['snippet']['publishedAt'], playlistId)
                print video_cmd
                cursor.execute(video_cmd)
                db.commit()

        try:
            nextPageToken = str(rv.json()['nextPageToken'])
        except:
            break
        url = 'https://www.googleapis.com/youtube/v3/playlistItems?maxResults=50&part=snippet&playlistId=%s&key=%s&pageToken=%s' % (playlistId, APIkey, nextPageToken)
