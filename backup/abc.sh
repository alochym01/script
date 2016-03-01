#!/bin/bash

target="/home/hadn"

for f in "$target"/*.ts
do
    echo "file '$f'" >> mylist.txt
done
