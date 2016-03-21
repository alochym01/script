from __future__ import division
from subprocess import Popen, PIPE
import shlex
from PIL import ImageFile
import os


def getsizes(fname):
    # get file size *and* image size (None if not known)
    file = open(fname)
    size = os.path.getsize(fname)
    p = ImageFile.Parser()
    while True:
        data = file.read(1024)
        if not data:
            break
        p.feed(data)
        if p.image:
            file.close()
            return p.image.size
    file.close()
    return size, None


def dimension_img(width, height, img, dimension):
    # dimension should be 16/9 = 1.78 or 4/3 = 1.34
    # should be normalize the image into 4:3 dimension and 16:9 dimension
    # using the ffmpeg -i input_img -vf "pad=800:450:(800-665)/2:(450-410)/2:Snow" out_img
    # pad=width:height:x:y - the pad should be bigger than dimension(width, height) of image
    flag = height * dimension
    if dimension > 1.7:
        if flag > width:
            pad = 'pad=%s:%s:%s:%s' % (flag, height, (flag-width)/2, 0)
        else:
            print 'go height flag=%s, height=%s' % (flag, height)
            value = width/1.78
            pad = 'pad=%s:%s:%s:%s' % (width, value, 0, value/2)
        cli = "ffmpeg -i %s -vf '%s:black' %s_%s.jpg -y" % (img, pad, img[:-4], 169)
    else:
        if flag > width:
            pad = 'pad=%s:%s:%s:%s' % (flag, height, (flag-width)/2, 0)
        else:
            print 'go height flag=%s, height=%s' % (flag, height)
            value = width/1.34
            pad = 'pad=%s:%s:%s:%s' % (width, value, 0, (value-height)/2)
        cli = "ffmpeg -i  %s -vf '%s:black' %s_%s.jpg -y" % (img, pad, img[:-4], 43)

    cli = shlex.split(cli)
    cmd = Popen(cli, stdout=PIPE).communicate()
    print cmd

with open('result.txt') as f:
    for line in f.readlines()[1:]:
        # real image file
        img = line.split('\n')[0]
        # get the width of image
        width, height = getsizes(img)
        for i in [1.78, 1.34]:
            print i
            dimension_img(width, height, img, i)
        break
