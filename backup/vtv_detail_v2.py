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


def upload_youtube(link,title,desc,keyword):
    os.chdir('/home/hadn/Downloads/adsense/vtv')
    wget.download(link)
    file_mp4 = link.split("/")[-1]
    cmd = '/home/hadn/Downloads/adsense/python/bin/python /home/hadn/Downloads/adsense/upload_youtube.py --file "%s" --title "%s" --description "%s" --keywords "%s" --category=25' % (file_mp4, title, desc, keyword)
    cmd = shlex.split(cmd.encode('utf8'))
    print cmd
    try:
        up = Popen(cmd, stdout=PIPE)
        temp = up.communicate()
        #: remove file which uploaded to youtube
        os.remove(file_mp4)
        return temp[0].split()[-4]
    except Exception as e:
        print str(e)
        pass


def upload_blogger(title, content, keywords, videoId):
    cmd = "/home/hadn/Downloads/adsense/python/bin/python /home/hadn/Downloads/adsense/blogger.py --title '%s' --content '%s' --labels '%s' --videoId %s" % (title, content, keywords, videoId)
    cmd = shlex.split(cmd.encode('utf8'))
    print cmd
    try:
        up = Popen(cmd, stdout=PIPE)
        print up.communicate()
    except Exception as e:
        print str(e)
        pass

def removeTag(content, tag):
    imgTag = ['<img(.*)>', '</img>', '<img(.*)/>', '<img(.*)/img>', '<div class="VCSortableInPreviewMode" (.*)>']
    aTag = ['href=(.*).htm" ', 'href=(.*).html" ']
    if tag.find('strong') != -1:
        temp = re.compile('<strong(.*)/strong>', re.DOTALL)
        return re.sub(temp, '', content)
    elif tag.find('table') != -1:
        temp = re.compile('<table(.*)/table>', re.DOTALL)
        return re.sub(temp, '', content)
    elif tag.find('script') != -1:
        temp = re.compile('<script(.*)/script>', re.DOTALL)
        return re.sub(temp, '', content)
    elif tag.find('img') != -1:
        for i in imgTag:
            temp = re.compile(i)
            content = re.sub(temp, '', content)
        return content
    elif tag.find('a') != -1:
        for i in aTag:
            temp = re.compile(i)
            content = re.sub(temp, 'href="http://xahoithethao.blogspot.com" ', content)
        return content
    return re.sub(temp, '', content)

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
except Exception as e:
    print str(e)

Tag = ['img', 'table', 'script', 'a', 'strong']
if link_mp4:
    keyw = ""
    content = soup.find("div", {"class":"clearfix mgt34"}).prettify()
    for i in Tag:
        content = removeTag(content, i)
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
    videoId = upload_youtube(link_mp4,title,desc,keyw)
    #upload_blogger(title, content, keyw, videoId)
