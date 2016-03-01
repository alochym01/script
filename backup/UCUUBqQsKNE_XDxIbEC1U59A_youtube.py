# -*- coding: utf8 -*-

#: syntax using: python UCUUBqQsKNE_XDxIbEC1U59A_youtube.py channel_id

from bs4 import BeautifulSoup, NavigableString
from youtube_dl import YoutubeDL
import json
import re
import sys
from subprocess import Popen, PIPE
import shlex
import os
import requests

def add_video_to_playlist(videoId):
    cmd = '/home/hadn/Downloads/adsense/python/bin/python /home/hadn/Downloads/adsense/donguyenha/playlist_football_item.py %s' % videoId
    cmd = shlex.split(cmd)
    print cmd
    try:
        up = Popen(cmd, stdout=PIPE)
        temp = up.communicate()
        print temp
    except Exception as e:
        print str(e)
        pass

def upload_blogger(title, content, keywords, videoId):
    cmd = "/home/hadn/Downloads/adsense/python/bin/python /home/hadn/Downloads/adsense/blogger.py --title '%s' --content '%s' --labels '%s' --videoId %s" % (title, content, keywords, videoId)
    cmd = shlex.split(cmd)
    print cmd
    print content
    try:
        up = Popen(cmd, stdout=PIPE)
        print up.communicate()
    except Exception as e:
        print str(e)
        print content
        pass

def xml_parse(entry, updatevideoId):
    '''The example data:
    <entry>
        <id>yt:video:_uY8ZvrBDRk</id>
        <yt:videoid>_uY8ZvrBDRk</yt:videoid>
        <yt:channelid>UCUUBqQsKNE_XDxIbEC1U59A</yt:channelid>
        <title>Luis SuÃ¡rez Goal -  Cordoba vs Barcelona 0-8 02.05.2015</title>
        <link href="http://www.youtube.com/watch?v=_uY8ZvrBDRk" rel="alternate"/>
        <author>
            <name>KoraLifeTV.HD</name>
            <uri>http://www.youtube.com/channel/UCUUBqQsKNE_XDxIbEC1U59A</uri>
        </author>
        <published>2015-05-02T15:09:16+00:00</published>
        <updated>2015-05-09T13:17:52+00:00</updated>
        <media:group>
            <media:title>Luis SuÃ¡rez Goal -  Cordoba vs Barcelona 0-8 02.05.2015</media:title>
            <media:content height="390" type="application/x-shockwave-flash" url="https://www.youtube.com/v/_uY8ZvrBDRk?version=3" width="640">
            <media:thumbnail height="360" url="https://i4.ytimg.com/vi/_uY8ZvrBDRk/hqdefault.jpg" width="480">
                <media:description>Luis SuÃ¡rez Goal FC -- Cordoba vs Barcelona 0-8 2015 Cordoba vs FC Barcelona 0-8 2015</media:description>
                <media:community>
                    <media:starrating average="4.60" count="10" max="5" min="1">
                        <media:statistics views="4169">
                        </media:statistics>
                    </media:starrating>
                </media:community>
            </media:thumbnail>
            </media:content>
        </media:group>
    </entry>'''
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
    print videoId, title, link
    return {
                "videoId" : videoId,
                "title" : title,
                "link" : link,
                "updated" : updated,
                "description" : "",
                "is_new" : 1
            }

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
            print json.dumps(rv, indent=2)
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
    #: all new video file which will be download by youtube-dl
    #: ydl_opts - should be check again, it now doesnot working :(
    ydl = YoutubeDL()
    os.getcwd()
    os.chdir('/home/hadn/Downloads/adsense/football/')
    ydl.add_default_info_extractors()
    for value in news:
        try:
            ydl.download([value['link']])
            for file_mp4 in os.listdir("/home/hadn/Downloads/adsense/football/"):
                if file_mp4.endswith(".mp4"):
                    cmd = '/home/hadn/Downloads/adsense/python/bin/python /home/hadn/Downloads/adsense/donguyenha-upload-youtube.py --file "/home/hadn/Downloads/adsense/football/%s" --title "%s" --description "%s"' % (file_mp4, value['title'], value['title'])
                    cmd = shlex.split(cmd)
                    #: upload video to Youtube
                    up = Popen(cmd, stdout=PIPE)
                    temp = up.communicate()
                    videoId = temp[0].split()[-4]
                    add_video_to_playlist(videoId)
                    #: remove file which uploaded to youtube
                    os.remove(file_mp4)
                    #upload_blogger(value['title'], value['title'], "football, da banh", videoId)
        except Exception, e:
            print str(e)
            pass
