#!/bin/bash
/home/hadn/python/bin/python /home/hadn/script/tuoitre_crawler/tuoitre.py $1

echo '' > /home/hadn/script/tuoitre_crawler/result.txt
target="/home/hadn/script/tuoitre_crawler/tuoitre"

for entry in "$target"/*/*.jpg
do
      echo "$entry" >> /home/hadn/script/tuoitre_crawler/result.txt
      echo "$entry"
done

#use python script to crop image into 2 size - small(w/h - 120:-1)/standard(640:-1)
#ffmpeg -i pho-nghe-vy-1457322572.jpg -vf scale=120:-1 pho-nghe-vy-1457322572-small.jpg
#ffmpeg -i pho-nghe-vy-1457322572.jpg -vf scale=640:-1 pho-nghe-vy-1457322572-standard.jpg
python image_normalize_standrad.py
python image_normalize_small.py
