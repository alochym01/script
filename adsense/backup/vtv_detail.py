from bs4 import BeautifulSoup
import urllib2
import shlex
import os
import wget
from subprocess import Popen, PIPE
from sys import argv
import re

def mysoup(link):
    url = urllib2.Request(link, headers={ 'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:33.0) Gecko/20100101 Firefox/33.0' })
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    return soup

def getMP4Link(temp_link):
    '''
        <div id="video-embeb">
        <div allowfullscreen="" frameborder="0" height="355" mozallowfullscreen="" msallowfullscreen="" oallowfullscreen="" scrolling="no" src="http://vcplayer.vcmedia.vn/1.1/?_site=vtv&amp;vid=vtv/ijz-bet8rewrytvvmh5s1vc2x6zbjm/2015/07/25/be-1437826646289-41b33.mp4&amp;_videoId=85846" webkitallowfullscreen="" width="650"></div>
        </div>
    '''
    temp_link = temp.div.get('src')
    pattern = re.compile('=vtv/(.*)mp4')
    link_key = 'http://hls.vcmedia.vn/%s' % re.search(pattern, temp_link).group().replace('=vtv', 'vtv')
    return link_key

def getMP4Link_v2(temp_link):
    '''
	<div class="VCSortableInPreviewMode" type="Video">
	 <div class="VCSortableInPreviewMode" data-height="400px" data-src="http://vcplayer.vcmedia.vn/1.1/?_site=vtv&amp;vid=vtv/tcpivs96jruta-ijtbu5dmzmrauar8/2015/07/25/9dh8iz1xae0-c923f.mp4&amp;autoplay=false&amp;_tag=http://vscc.hosting.vcmedia.vn/tag/0078066a02a64593822ebd9dc70ed416" data-width="600px" id="videoid_85866" type="VideoStream" videoid="85866">
	 </div>
	 <div>
	  <p style="text-align: center;">
	  </p>
	 </div>
	</div>
    '''
    temp_link = temp.div.get('data-src')
    pattern = re.compile('=vtv/(.*)mp4')
    link_key = 'http://hls.vcmedia.vn/%s' % re.search(pattern, temp_link).group().replace('=vtv', 'vtv')
    return link_key

def upload_youtube(link,title,desc,keyword):
    os.chdir('/home/hadn/Downloads/adsense/vtv')
    wget.download(link)
    file_mp4 = link.split("/")[-1]
    cmd = '/home/hadn/Downloads/adsense/python/bin/python /home/hadn/Downloads/adsense/upload_youtube.py --file "%s" --title "%s" --description "%s" --keywords "%s" --category=25' % (file_mp4, title, desc, keyword)
    cmd = shlex.split(cmd.encode('utf8'))
    print cmd
    try:
        up = Popen(cmd, stdout=PIPE)
        print up.communicate()
        #: remove file which uploaded to youtube
        os.remove(file_mp4)
    except Exception as e:
        print str(e)
        pass


soup = mysoup(argv[1])
getinfos = soup.find("div",{"class":"inner"})
title = getinfos.find("h1",{"class":"news-title"}).string.replace("''","'").replace('"','\'')
try:
    desc = getinfos.find("h2",{"class":"news-sapo"}).string.replace("''","'").replace('"','\'').replace("VTV.vn -","")
except:
    desc = title
try:
    pattern_film = re.compile('=vtv/(.*).mp4')
    link_mp4 = 'http://hls.vcmedia.vn/%s' % re.search(pattern_film, str(soup)).group().replace('=vtv', 'vtv')
    '''temp = soup.find("div",{"id":"video-embeb"})
    if temp:
        print "TEMP OK \t\t"
        link_mp4 = getMP4 Link(temp)
    else:
        print "TEMP NOT OK \t\t"
        temp = soup.find("div", {"class":"VCSortableInPreviewMode"})
        link_mp4 = getMP4Link_v2(temp)
        print link_mp4'''
except Exception as e:
    print str(e)

if link_mp4:
    keyw = ""

    try:
        tags = soup.find("div",{"class":"tag"}).find_all("li")
    except:
        tags = ['tintuc, vtv']

    try:
        for tag in tags:
            if len(tag.string) < 30:
                keyw += ","+ tag.string
    except:
        pass
    #print title.encode('utf-8'), link_mp4
    #print keyw.encode('utf-8'), desc.encode('utf-8')
    upload_youtube(link_mp4,title,desc,keyw)
