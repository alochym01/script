import time
from urllib import urlopen
import m3u8
import os
import shlex
from subprocess import Popen, PIPE

data = urlopen("http://118.69.252.4/tv/htv7HD/index.m3u8").read()
obj = m3u8.loads(data)
now = time.strftime('%Y%m%d', time.localtime())
#time is 11:45 AM to 12:00
start_time = int(now + '044800')
end_time = int(now + '050500')
#end_time = int(now + '015500')
#file = '/home/hadn/ffmpeg/'
file = '/opt/hadn/monngon/'
fileList = []
for val in obj.segments:
    uri = int((time.strftime('%Y%m%d%H%M%S', time.gmtime(float(val.uri.split('.ts')[0])/1000))))
    if uri > start_time and uri < end_time:
        url = "http://118.69.252.4/tv/htv7HD/%s" % val.uri
        print url
        #: save all file which mat condition
        file_name = file + val.uri
        #: put all file ts into a list
        fileList.append(file_name)
        with open(file_name, 'w') as f:
            url = "http://118.69.252.4/tv/htv7HD/%s" % val.uri
            f.write(urlopen(url).read())

cmd = 'ffmpeg -i "concat:%s" -y -c copy -bsf:a aac_adtstoasc /opt/hadn/monngon/mon_ngon_moi_ngay_%s.mp4' % ('|'.join(fileList), now)
cmd = shlex.split(cmd)
result = Popen(cmd, stdout=PIPE)
#print 'success: %s,\terror: %s' % result.communicate()
