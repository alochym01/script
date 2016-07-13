from pymongo import MongoClient
import pycurl
import json
from StringIO import StringIO
import time
from urllib import urlopen
import m3u8
import os
import shlex
from subprocess import Popen, PIPE
from datetime import date, timedelta
import re
import sys
import time
import urllib
import urllib2
import requests

def curl(url) :
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()

    body = buffer.getvalue()
    return body

def downloadM3u8(url, filmId) :
 #  url = 'http://s3.amazonaws.com/_bc_dml/example-content/tears-of-steel/playlist.m3u8'
  #  url = 'http://plist.vn-hd.com/mp4v3/4055ec62f2d3860ca57a174c121fee03/8502305be2574cf3bbd82fb3f122334f/035c135af6eb46338a22f9c4642d9e6a/10115_e1_320_1280_ivdc.smil/playlist.m3u8'
    fileList = []
    print url
    filePath = '/Users/giaule/Crawler/';
    filePathFilm = filePath + 'films/';
    lines = url.split("/")
    lastLine = lines[-1]
    urlPath = url.replace(lastLine, '')
    print urlPath
    data = urlopen(url).read()
    
    if data.find('m3u8') <> -1 :
        line = data.split("\n")
        if line[-1] == '':
            m3u8Link = line[len(line) - 2]
        else:
            m3u8Link = line[-1]

        if m3u8Link.find('http://') <> -1:
            url = m3u8Link
        else:
            url  = urlPath + m3u8Link
        print url
        data = urlopen(url).read()
        lines = url.split("/")
        lastLine = lines[-1]
        urlPath = url.replace(lastLine, '')
        
    print data
    obj = m3u8.loads(data)
    now = (date.today() - timedelta(1)).strftime('%Y%m%d')
    for val in obj.segments:
        uri = val.uri
        
        urlCrawler = urlPath + val.uri
        fileName = filePath + val.uri

        if uri.find('http://') <> -1:
            urlCrawler = uri
            uris = uri.split("/")
            fileName = filePath + uris[-1]
        else:
            urlCrawler = urlPath + uri
            fileName = filePath + uri
        
        fileList.append(fileName)

        with open(fileName, 'w') as f:
            url = urlPath + val.uri
            print url
            f.write(urlopen(urlCrawler).read())
            
        print val.uri
    fileName = filePathFilm + '%s.mp4' % filmId
    cmd = '/Users/giaule/Softs/ffmpeg -i "concat:%s" -y -c copy -bsf:a aac_adtstoasc %s' % ('|'.join(fileList), fileName)
    print cmd
    cmd = shlex.split(cmd)
    result = Popen(cmd, stdout=PIPE)

def downloadGoogle(url, filmId):
    filePath = '/Users/giaule/Crawler/';
    filePathFilm = filePath + 'films/';
    fileName = filePathFilm + '%s.mp4' % filmId
    response = urllib.urlopen(url)

    total = int(response.info().getheader('Content-Length').strip())
    status_string = ('  {:,} Bytes [{:.2%}] received. Rate: [{:4.0f} '
                     'kbps].  ETA: [{:.0f} secs]')
    chunksize, bytesdone, t0 = 16834, 0, time.time()
    outfh = open(fileName, 'wb')
    progress = True;
    while 1:
        chunk = response.read(chunksize)
        elapsed = time.time() - t0
        outfh.write(chunk)
        bytesdone += len(chunk)
        if not chunk:
            outfh.close()
            break
        if progress:
            rate = (bytesdone / 1024) / elapsed
            eta = (total - bytesdone) / (rate * 1024)
            display = (bytesdone, bytesdone * 1.0 / total, rate, eta)
            status = status_string.format(*display)
            sys.stdout.write("\r" + status + ' ' * 4 + "\r")
            sys.stdout.flush
            
client = MongoClient()
db = client['alofilm_final']
while 1:
    film = db.films.find_one({"myself_status": "new"})

    if film is None:
        break

    db.films.update_one(
        {"_id": film['_id']},
        {
            "$set": {
                "myself_status": "processing"
            }
        }
    );

    filmId = film['crawler_film_id']
    files = film['files']
    series = 1;
    streamingFiles = [];
    subtitles = [];
    for file in files:
        url = 'http://my.crawler.alofilm.club/get-link.php?filmId=%s&series=%s' % (filmId, series);
        streamingFile = {}
        linkInfo = json.loads(curl(url))
        
        if linkInfo['subtitle'] :
            subtitles = linkInfo['subtitle']
            
        if linkInfo is not None:
            if linkInfo['level']:
                lastLabelFilm = linkInfo['level'][-1]['file']
            else:
                lastLabelFilm = linkInfo['file']
            streamingFile['file'] = lastLabelFilm
            streamingFiles.append(streamingFile)

 #          lastLabelFilm = 'http://plist.vn-hd.com/mp4v3/4055ec62f2d3860ca57a174c121fee03/8502305be2574cf3bbd82fb3f122334f/035c135af6eb46338a22f9c4642d9e6a/10115_e1_320_1280_ivdc.smil/playlist.m3u8'

            print lastLabelFilm.find('m3u8')
            fileName = '%s-%s' % (filmId, series)
            if lastLabelFilm.find('m3u8') <> -1 :
                downloadM3u8(lastLabelFilm, fileName)
            else:
                downloadGoogle(lastLabelFilm, fileName)
        series = series + 1
        print streamingFiles;
            
    urlCrawler = film['crawler_link']

    # update trang thai
    db.films.update_one(
        {"_id": film['_id']},
        {
            "$set": {
                "myself_status": "completed"
            }
        }
    );
    #print(film)
