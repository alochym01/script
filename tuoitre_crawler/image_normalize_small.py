from subprocess import Popen, PIPE
import json
import shlex

with open('result.txt') as f:
    for line in f.readlines()[1:]:
        # real image file
        img = line.split('\n')[0]
        # string remove '/' put it into a slug(list)
        slug = line.split('/')
        # the path of json file
        path = '/'.join(slug[:-1])
        filename = '%s/%s.html' % (path, slug[-2])
        try:
            with open(filename) as f:
                video = json.loads(f.read())
            # ffmpeg commandline
            small_cmd = 'ffmpeg -y -i %s  -vf scale=120:-1 %s/%s-small.jpg' % (img, path, video['items'][0]['etag'])
            small_cmd = shlex.split(small_cmd)
            small = Popen(small_cmd, stdout=PIPE).communicate()
            print small
        except Exception as e:
            print str(e)
