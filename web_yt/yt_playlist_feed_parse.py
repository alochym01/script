import json
import requests
from bs4 import BeautifulSoup, NavigableString

def yt_video_parse(data):
    return {
        "videoId" : data['yt:videoid'],
        "title" : data['title'],
        "link" : "http://www.youtube.com/watch?v=%s" % data['yt:videoid'],
        "updated" : data['updated'],
        "description" : data['media:description'],
        "is_new" : 1
        }

playlist_feed_url = 'https://www.youtube.com/feeds/videos.xml?playlist_id=PLiYWpBi4dlS-BvSE7gVw5U4_9XDL94FKT'

rv = requests.get(playlist_feed_url)

soup = BeautifulSoup(rv.content)

temp = soup.findAll('entry')

data = []

for t in temp:
    t_dict = {}
    for entry in t.descendants:
      if not isinstance(entry, NavigableString):
        #print '%s===\t%s' % (entry.name, entry.text)
        t_dict.update({entry.name: entry.text})
    print json.dumps(yt_video_parse(t_dict), indent=2)
