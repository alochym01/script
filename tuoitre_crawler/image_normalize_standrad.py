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
            standard_cmd = 'ffmpeg -y -i %s  -vf scale=640:-1 %s/%s-standard.jpg' % (img, path, video['items'][0]['etag'])
            standard_cmd = shlex.split(standard_cmd)
            standard = Popen(standard_cmd, stdout=PIPE).communicate()
            print standard
        except Exception as e:
            print str(e)
