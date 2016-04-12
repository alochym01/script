# -*- coding: utf8 -*-

import json
import re
import sys
from subprocess import Popen, PIPE
import shlex
import os
import requests


#<item>
#<title>Xem thoải mái – Nhận ngay ưu đãi của VTVcab</title>
#<description>...</description>
#<link>...</link>
#<pubDate>Tuesday, April 12, 2016 (GMT+7)</pubDate>
#</item>

pattern = re.compile('<link/>(.*)<pubdate>')
url = 'http://ictnews.vn/rss/vien-thong'
data = requests.get(url)
from bs4 import BeautifulSoup, NavigableString
soup = BeautifulSoup(data.content, "html5lib")
for item in soup.channel.copyright.next_siblings:
    print item.title
    print item.description
    #print item.link
    print 'link %s' % re.sub('<link/>|<pubdate>','', pattern.search(str(item)).group())
    print item.pubdate
