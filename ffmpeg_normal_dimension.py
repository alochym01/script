"""
    Wanted dimension image is 4:6
"""

temp_path = '/home/hadn/test.jpg'
temp_path_ffmpeg = '/home/hadn/ffmpeg/test.jpg'

def img_normalize(temp_path, img_path_ffmpeg):
    im = imageio.imread(temp_path)
    img_h, img_w, img_v = im.shape
    print img_h, img_w
    if img_w/img_h > 0.66666:
        value = img_h*2/3
        value_crop = img_w - value
        cmd = '/usr/bin/ffmpeg -i %s -vf "crop=%s:ih:%s/2:ih/2" %s -y' % (temp_path, value, value_crop, img_path_ffmpeg)
    else:
        value = img_w*3/2
        print value
        value_crop = img_h - value
        cmd = '/usr/bin/ffmpeg -i %s -vf "crop=iw:%s:iw/2:%s/2" %s -y' % (temp_path, value, value_crop, img_path_ffmpeg)
    cmd = shlex.split(cmd)
    print cmd
    process = Popen(cmd, stdout=PIPE)
    process.wait()
    cmd_normalize = '/usr/bin/ffmpeg -i %s -vf scale=400:-1 %s -y' % (img_path_ffmpeg, temp_path)
    cmd_normalize = shlex.split(cmd_normalize)
    print cmd_normalize_640
    process = Popen(cmd_normalize, stdout=PIPE)
    process.wait()
    return True

img_normalize(temp_path, img_path_ffmpeg)
