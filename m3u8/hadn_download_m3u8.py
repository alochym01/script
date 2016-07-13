#!/usr/bin/env python
# -*- coding: utf-8 -*-
import m3u8
import cfscrape
import os
import execjs
import re

# get javascript execute env
default = execjs.get()

# set default folder to store ts files
temp_folder = '/home/hadn/'
url = 'http://hdonline.vn/phim-truong-an-tam-quai-tham-tap-2-12257.100647.html'
scraper = cfscrape.create_scraper()
crawler = scraper.get(url)

# should be continued with html parse
# get the link to download file m3u8
link_m3u8 = getlink(crawler.content)

# link reference https://tools.ietf.org/html/draft-pantos-http-live-streaming-19#section-8.7
m3u8_obj = m3u8.load(link_m3u8)
try:
    # the playlist is sort by ordering resolution of film
    # m3u8_obj.playlists[0].stream_info.resolution
    m3u8_final_link = m3u8_obj.playlists[0].absolute_uri
    film_folder = '%s%s' % (temp_folder, m3u8_obj.playlists[0].base_path)
except:
    # the m3u8_obj is not multi profiles
    m3u8_final_link = m3u8_obj.absolute_uri
    film_folder = '%s%s' % (temp_folder, m3u8_obj.base_path)

# download the highest profile m3u8
# get current directory
os.getcwd()
os.mkdir(film_folder)

# change to film folder
os.chdir(film_folder)
obj = m3u8.loads(m3u8_final_link)
