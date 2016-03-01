import os
import shlex
from youtube_dl import YoutubeDL
from subprocess import Popen, PIPE
from sys import argv
from bs4 import BeautifulSoup
import requests

for i in argv[1:]:
    data = requests.get(i)
    soup = BeautifulSoup(data.content)
    title = str(soup.title.text)
    print title
    os.getcwd()
    os.chdir('/home/hadn/Downloads/adsense/football/')
    ydl = YoutubeDL()
    ydl.add_default_info_extractors()
    try:
        print i
        ydl.download([i])
        for file_mp4 in os.listdir("/home/hadn/Downloads/adsense/football/"):
            if file_mp4.endswith(".mp4"):
                cmd = '/home/hadn/Downloads/adsense/python/bin/python /home/hadn/Downloads/adsense/donguyenha-upload-youtube.py --file "/home/hadn/Downloads/adsense/football/%s" --title "%s" --description "%s"' % (file_mp4, title, title)
                cmd = shlex.split(cmd)
                print cmd
                #: upload video to Youtube
                up = Popen(cmd, stdout=PIPE)
                temp = up.communicate()
                videoId = temp[0].split()[-4]
                #: remove file which uploaded to youtube
                os.remove(file_mp4)
                #upload_blogger(value['title'], value['title'], "football, da banh", videoId)
    except Exception, e:
        print str(e)
        pass
