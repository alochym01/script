from bs4 import BeautifulSoup, NavigableString
import requests
import urllib2
from sys import argv

#url = 'http://video.vnexpress.net/the-gioi/trung-quoc-xay-dung-trai-phep-tren-bien-dong-nhu-the-nao-3221084.html'
url = argv[-1]

data = requests.post(url)

soup = BeautifulSoup(data.content)

for video in soup.findAll('param'):
    if video['name'] == 'flashvars':
        #print video['value']
        for link in video['value'].split('='):
            if link.find('objectid') != -1:
                video_link = link.split('&')[0].encode('utf-8')
                break
file = '/home/hadn/Downloads/adsense/%s' % video_link.split('/')[-1]
r = urllib2.urlopen(video_link)
with open(file, 'w') as f:
    print 'writing ....'
    f.write(r.read())
