#!/bin/bash
export http_proxy="http://proxy.hcm.fpt.vn:80"
export https_proxy="https://proxy.hcm.fpt.vn:80"

i=1
cd ~
for item in /home/hadn/Downloads/adsense/yt.thegioi/aws/*.json
do
     echo "Item $((i++)) : $item"
     /home/hadn/python/bin/aws s3 cp $item s3://xemtin.xyz/crawling/videos/pending/vtv/  --profile xemtin_xyz_crawling  --content-type application/json
     mv $item /home/hadn/Downloads/adsense/yt.thegioi/awsupload/
done
