#!/bin/bash

target="/home/hadn/script/tuoitre/"

for file in $*
do
    echo "file '$f'"
    echo "file '$f'" >> mylist.txt
    [ -f "$file"  ] && echo "$file"
done
for entry in "$target"/*/*.jpg
do
      echo "$entry"
      echo "$entry'_smale'"
done
