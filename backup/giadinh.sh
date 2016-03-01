#!/bin/bash
export http_proxy="http://210.245.31.15:80"
now=$(date +"%m_%d_%Y")
ffmpeg -i http://118.69.252.4/tv/htv7HD/index.m3u8 -strict -2 -t 1200 /home/hadn/Downloads/adsense/buacom_$now.mp4
