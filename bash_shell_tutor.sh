#!/bin/bash

echo '' > result.txt
target="/home/hadn/script/tuoitre"

for entry in "$target"/*/*.jpg
do
      echo "$entry" >> result.txt
      echo "$entry"
done

#use python script to crop image into 2 size - small(w/h - 120:-1)/standard(640:-1)
#ffmpeg -i pho-nghe-vy-1457322572.jpg -vf scale=120:-1 pho-nghe-vy-1457322572-small.jpg
#ffmpeg -i pho-nghe-vy-1457322572.jpg -vf scale=640:-1 pho-nghe-vy-1457322572-standard.jpg

with open('result.txt') as f:
    for line in f.readlines():
        slug = line.split('/')
        print '/'.join(slug[:-1])

from subprocess import Popen, PIPE
import json
import shlex

with open('result.txt') as f:
    for line in f.readlines()[1:]:
        img = line.split('\n')[0]
        slug = line.split('/')
        path = '/'.join(slug[:-1])
        filename = '%s/%s.html' % (path, slug[-2])
        try:
            with open(filename) as f:
                video = json.loads(f.read())
            small_cmd = 'ffmpeg -y -i %s  -vf scale=120:-1 %s/%s-small.jpg' % (img, path, video['items'][0]['etag'])
            small_cmd = shlex.split(small_cmd)
            standard_cmd = 'ffmpeg -y -i %s  -vf scale=640:-1 %s/%s-standard.jpg' % (img, path, video['items'][0]['etag'])
            standard_cmd = shlex.split(standard_cmd)
            up = Popen(cmd, stdout=PIPE).communicate()
            print up
        except Exception as e:
            print str(e)


