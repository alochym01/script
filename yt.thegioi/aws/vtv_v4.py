from bs4 import BeautifulSoup
import urllib2
import shlex
import os
import re
import wget
import requests
from subprocess import Popen, PIPE

def mysoup(link):
    url = urllib2.Request(link, headers={ 'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:33.0) Gecko/20100101 Firefox/33.0' })
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read(), "html5lib")
    return soup


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
            content = re.sub(temp, 'href="http://xemtin.xyz" ', content)
        return content
    return re.sub(temp, '', content)


def upload_blogger(title, content, keywords, videoId):
    cmd = "/home/hadn/python/bin/python /home/hadn/Downloads/adsense/blogger.py --title '%s' --content '%s' --labels '%s' --videoId %s" % (title, content, keywords, videoId)
    cmd = shlex.split(cmd.encode('utf8'))
    print cmd
    try:
        up = Popen(cmd, stdout=PIPE)
        print up.communicate()
    except Exception as e:
        print str(e)
        pass


def upload_youtube(link,title,desc,keyword):
    os.chdir('/home/hadn/Downloads/adsense/yt.thegioi')
    wget.download(link)
    file_mp4 = link.split("/")[-1]
    cmd = '/home/hadn/python/bin/python /home/hadn/Downloads/adsense/yt.thegioi/upload_youtube.py --file "%s" --title "%s" --description "%s" --keywords "%s" --category=25' % (file_mp4, title, desc, keyword)
    cmd = shlex.split(cmd.encode('utf8'))
    print cmd
    try:
        up = Popen(cmd, stdout=PIPE)
        temp = up.communicate()
        print temp
        #: remove file which uploaded to youtube
        os.remove(file_mp4)
        return temp[0].split()[-4]
    except Exception as e:
        print str(e)
        pass

def add_video_to_playlist(videoId, playlistId):
    cmd = '/home/hadn/python/bin/python /home/hadn/Downloads/adsense/yt.thegioi/playlist_item.py --videoId %s --playlistId %s' % (videoId, playlistId)
    cmd = shlex.split(cmd)
    print cmd
    try:
        up = Popen(cmd, stdout=PIPE)
        temp = up.communicate()
        print temp
    except Exception as e:
        print str(e)
        pass

soup = mysoup("http://vtv.vn/truyen-hinh-truc-tuyen.htm")
videos_new = soup.find("div",{"class":"video-news-box"}).find("ul",{"class":"list-item"}).find_all("li")

links = []

for video in videos_new:
    link = "http://vtv.vn"+video.find("a").get("href")
    links.append(link)

if not links:
    sys.exit(0)

with open('/home/hadn/Downloads/adsense/yt.thegioi/aws/vtv.txt') as f:
    link_traced = f.readlines()[0].split(',')

index = 0
for link in links:
    if link in link_traced:
        break
    index += 1

if index > 0:
    with open('/home/hadn/Downloads/adsense/yt.thegioi/aws/vtv.txt', 'w') as f:
        f.write(','.join(links[:index]))

#chym = ['bat-dong-san', 'cac-mon-khac', 'chinh-tri', 'chuyen-dong-24h', 'cong-nghe', 'cuoc-song-thuong-ngay', 'doi-song', 'du-lich', 'giao-duc', 'kinh-te', 'moi-ngay-mot-cuon-sach', 'phap-luat', 'san-pham', 'suc-khoe', 'tai-chinh', 'tam-long-viet', 'toan-canh-the-gioi', 'the-gioi-do-day', 'the-gioi', 'thi-truong', 'tin-tuc', 'trong-nuoc', 'tu-van', 'van-de-hom-nay', 'viet-nam-va-the-gioi', 'xa-hoi', 'gioi-tinh', 'dang-trong-cuoc-song-hom-nay', 'su-kien-va-binh-luan', 'dan-hoi-bo-truong-tra-loi']

chym = ['chuyen-dong-24h', 'xa-hoi']
abc_links = []

for link in links[:index]:
    temp = link.split('/')[3]
    if temp in chym:
        print link
        print temp
        abc_links.append(link)

#for link in links[:index]:
for link in abc_links:
    try:
        soup = mysoup(link)
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
        desc = "Website: http://xemtin.xyz" + desc
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
                #videoId = upload_youtube(link_mp4,title,desc,keyw)
            except Exception as e:
                print str(e)
                pass
            #upload_blogger(title, content, keyw, videoId)
            videoId = upload_youtube(link_mp4,title,desc,keyw)
            aws_url = 'https://www.googleapis.com/youtube/v3/videos?id=%s&key=AIzaSyBJfbeKEvD06WAS1AnRD4kMyCQ5rjmnSMs&part=snippet' % videoId.split("'")[1]
            print aws_url
            rv = requests.get(aws_url)
            filename = '/home/hadn/Downloads/adsense/yt.thegioi/aws/%s.json' % videoId.split("'")[1]
            f = open (filename, 'w')
            f.write(rv.text.encode('utf8'))
            f.close()
            temp = link.split('/')[3]
            add_video_to_playlist(videoId, temp)
    except:
        pass
