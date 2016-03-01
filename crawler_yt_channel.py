# -*- coding: utf8 -*-
import requests
import MySQLdb
import json


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
    
    for k,v in data.items():
         if k.find("thumbnails") != -1:
            thumbnails = json.dumps(v)
         elif k.find("title") != -1:
            title = json.dumps(v)
         elif k.find("channelId") != -1:
            channelId = json.dumps(v)
         elif k.find("publishedAt") != -1:
            publishedAt = json.dumps(v)
         elif k.find("channelId") != -1:
            channelId = json.dumps(v)
         elif k.find("description") != -1:
            description = json.dumps(v)
         elif k.find("resourceId") != -1:
            videoId = json.dumps(v["videoId"])
            '''
    temp = {
                "thumbnails" : json.dumps(data["thumbnails"]),
                "title" : json.dumps(data["title"]),
                "publishedAt" : json.dumps(data["publishedAt"]),
                "channelId" : json.dumps(data["channelId"]),
                "description" : json.dumps(data["description"]),
                "videoId" : json.dumps(data["resourceId"]["videoId"]),
                "youtubeId" : data["resourceId"]["videoId"],
            }
    #print json.dumps(temp, indent=2)
    return temp
  

with open('/mnt/svn_script/api_public_key.txt') as f:
    APIkey = f.read().strip()
    
with open('/mnt/svn_script/channel_ID.txt') as f:
    channelId = f.read().strip()

print APIkey
url = 'https://www.googleapis.com/youtube/v3/search?order=date&part=snippet&channelId=%s&maxResults=25&key=%s' % (channelId, APIkey)
url = 'https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id=%s&key=%s' % (channelId, APIkey)

#: sql config
#: username: root
#: password: abc@123

db = MySQLdb.connect(host="localhost",user="root", passwd="abc@123",db="alokids", use_unicode=True, charset='utf8')
cursor = db.cursor()

rv = requests.get(url)
playlistId = rv.json()['items'][0]["contentDetails"]["relatedPlaylists"]["uploads"]
count = 1
url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=%s&key=%s' % (playlistId, APIkey)
while True:
    rv = requests.get(url)
    items = rv.json()['items']
    for i in items:
        temp = channelDetails(i["snippet"])
        #sql_cmd = 'INSERT INTO videos(title, description, youtubechannelId, streamUrl, youtubeId, thumbnails_json) VALUES(%s, %s, %s, \"https://www.youtube.com/watch?v=%s\", %s, \'%s\')' % (temp["title"], temp["description"], temp["channelId"], temp["videoId"].split('"')[1], temp["videoId"], temp["thumbnails"])
        sql_cmd = 'INSERT INTO videos(\
                    title,\
                    description,\
                    youtubechannelId,\
                    streamUrl,\
                    youtubeId,\
                    thumbnails_json)\
                VALUES(%s, %s, %s, \"https://www.youtube.com/watch?v=%s\", %s, \'%s\')'\
                % (temp["title"],\
                temp["description"],\
                temp["channelId"],\
                temp["youtubeId"],\
                temp["videoId"],\
                temp["thumbnails"])
        print sql_cmd
        cursor.execute(sql_cmd)
        db.commit()
    nextPageToken = str(rv.json()['nextPageToken'])
    url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=%s&key=%s&pageToken=%s' % (playlistId, APIkey, nextPageToken)
    print nextPageToken
    print url
db.close()
