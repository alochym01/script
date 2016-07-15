#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    how to run from console: python m3u8_download.py link_crawler path_to_folder filmid film_folder
    example:
    python m3u8_download.py http://hdonline.vn/phim-tim-lai-chinh-minh-tap-2-7746.63001.html /home/hadn/film/ 7746 Kill_Me_Heal_Me 2
'''
import m3u8
import os
import re
import shlex
from subprocess import PIPE, Popen
import requests
from sys import argv

def M3U8link(content, temp_folder):
    temp_file_name = '%s%s' % (temp_folder, 'file_m3u8.m3u8')
    with open(temp_file_name, 'wb') as f:
        f.write(content)
    return temp_file_name

# set default folder to store ts files
url = argv[1]
temp_folder = argv[2]
filmId = argv[3]
film_folder = '%s%s' % (temp_folder, argv[4])
episode = argv[5]
film_name = "%s-%s" % (filmId, episode)
# set list User-Agent
DEFAULT_USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"
]

# should be continued with html parse
headers_request = [{'User-Agent': DEFAULT_USER_AGENTS[0]},
                    {'Accept-Encoding' : 'gzip, deflate, sdch'},
                    {'Accept-Language': 'en-US,en;q=0.8'}]
session = requests.session()
for header in headers_request:
    session.headers.update(header)

# get data of html and then save data into output.txt for getting token from php script
# if know javascript function and can be execute by execjs in python
html_content = session.get(url)
file_html = '%s%s' % (temp_folder, 'output.txt')
with open(file_html, 'wb') as f:
    f.write(html_content.text.encode('utf-8'))

# run php cli to get token key
cmd = "php get-token.php %s" % (file_html)
cmd = shlex.split(cmd)
up = Popen(cmd, stdout=PIPE)
token = up.stdout.readlines()[-1].split('"')[1]

# update headers request for query real m3u8 link
headers_request_v1 = [{'Referer': url},
                    {'Connection' : 'keep-alive'},
                    {'X-Requested-With': 'XMLHttpRequest'},
                    {'Keep-Alive': 300},
                    {'Accept' : 'application/json, text/javascript, */*; q=0.01'}]
for header in headers_request_v1:
    session.headers.update(header)

url_link = 'http://hdonline.vn/frontend/episode/xmlplay?ep=%s&fid=%s&token=%s&_x=0.875115562264676&format=json' % (episode, filmId, token)

# get the link to download file m3u8
file_m3u8 = session.get(url_link).json()['file']
print file_m3u8

# update session header again to requests playlist.m3u8
session.headers.update({'X-Requested-With': 'ShockwaveFlash/22.0.0.209'})
session.headers.update({'Accept' : '*/*'})

# get real link m3u8
temp_m3u8 = session.get(file_m3u8)
'''
playlist with multi profiles start playlist_m.m3u8 and content sample:

hdonline condition:
profile: 720p(HD) - VIP only
profile: 480p(SD) - login only
profile: 360p(SD) - no login
    #EXTM3U
    #EXT-X-VERSION:3
    #EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2500000,CODECS="avc1.100.41,mp4a.40.2",RESOLUTION=1280x720
    Truong_An_Tam_Quai_Tham_720p_ViE_E002_1024/playlist.m3u8
    #EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1300000,CODECS="avc1.77.31,mp4a.40.2",RESOLUTION=800x450
    Truong_An_Tam_Quai_Tham_720p_ViE_E002_800/playlist.m3u8
    #EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=800000,CODECS="avc1.77.31,mp4a.40.2",RESOLUTION=640x360
    Truong_An_Tam_Quai_Tham_720p_ViE_E002_640/playlist.m3u8
'''

# playlist only 1 profile - 360p
'''
    #EXTM3U
    #EXT-X-STREAM-INF:RESOLUTION=0x0
    list.m3u8
'''
playlist_m3u8 = temp_m3u8.text.split('\n')
if len(playlist_m3u8) > 3:
    print "getting highest profiles ================"
    # save response content into file for m3u8 load later
    temp_file_name = M3U8link(temp_m3u8.text, temp_folder)
    m3u8_obj = m3u8.load(temp_file_name)
    # the playlist is sort by ordering resolution of film
    # m3u8_obj.playlists[0].stream_info.resolution - highest profile
    m3u8_final_link = m3u8_obj.playlists[0].uri
    hadn_m3u8 = re.sub('playlist_m.m3u8', m3u8_final_link, temp_m3u8.url)
    # last m3u8 link
    result_m3u8 = session.get(hadn_m3u8)
    # save response content into file for m3u8 load later
    temp_file_name = M3U8link(result_m3u8.text, temp_folder)
    # link reference https://tools.ietf.org/html/draft-pantos-http-live-streaming-19#section-8.7
    m3u8_obj = m3u8.load(temp_file_name)
    # the media files
    ts_files = m3u8_obj.files
else:
    print "getting default profiles ================"
    link =playlist_m3u8[-1]
    # last m3u8 link
    hadn_m3u8 = re.sub('playlist.m3u8', link, temp_m3u8.url)
    result_m3u8 = session.get(hadn_m3u8)
    # save response content into file for m3u8 load later
    temp_file_name = M3U8link(result_m3u8.text, temp_folder)
    # link reference https://tools.ietf.org/html/draft-pantos-http-live-streaming-19#section-8.7
    m3u8_obj = m3u8.load(temp_file_name)
    # the media files
    ts_files = m3u8_obj.files

# get current directory
os.getcwd()
try:
    os.mkdir(film_folder)
except:
    pass
# change to film folder
os.chdir(film_folder)

link_ts = re.sub('\w+.m3u8$', '', result_m3u8.url)
for i in ts_files:
    url = '%s%s' % (link_ts, i)
    r = session.get(url)
    print url
    with open(i, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

cmd = 'ffmpeg -i "concat:%s" -y -c copy -bsf:a aac_adtstoasc %s.mp4' % ('|'.join(ts_files), film_name)
cmd = shlex.split(cmd)
# get too many files open error - check link below
# https://singztechmusings.wordpress.com/2011/07/11/ulimit-how-to-permanently-set-kernel-limits-in-linux/
result = Popen(cmd, stdout=PIPE)


# do more step upload film to google drive, remove film_folder and update mongodb
