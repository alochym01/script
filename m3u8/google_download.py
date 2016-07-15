import requests
import os
from sys import argv

def Google(url, film_folder, film_name):
    os.mkdir(film_folder)
    filename = '%s/%s' % (film_folder, film_name)
    try:
        r = requests.get(url, stream=True)
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    #f.flush() commented by recommendation from J.F.Sebastian
        return local_filename
    except Exception as e:
        print str(e)

url = argv[1]
temp_folder = argv[2]
filmId = argv[3]
film_folder = argv[4]
episode = argv[5]

temp_folder = "%s%s" % (temp_folder, film_folder)
film_name "%s-%s" %(filmId, episode)
print url
print temp_folder
print film_name
Google(url, temp_folder, film_name)

# do more step upload film to google drive and update mongodb
