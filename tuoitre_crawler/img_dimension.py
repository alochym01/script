import ImageFile
import os
import sys
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

print getsizes(sys.argv[-1])
