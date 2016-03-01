#!/bin/bash
export http_proxy="http://210.245.31.15:80"
export https_proxy="https://210.245.31.15:80"
echo $1
/home/hadn/Downloads/adsense/python/bin/python /home/hadn/Downloads/adsense/dl_vtv.py $1
