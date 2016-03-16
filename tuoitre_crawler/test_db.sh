#!/bin/bash
target="/home/hadn/script/tuoitre_crawler/tuoitre"

for entry in "$target"/*/*.html
do
    echo "$entry" >> /home/hadn/script/tuoitre_crawler/html.txt
    echo "$entry"
done

