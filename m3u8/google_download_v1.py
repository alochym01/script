from subprocess import Popen, PIPE
import shlex
import requests
from pymongo import MongoClient
import os

DEFAULT_USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"
]

'''
    Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
    Accept-Encoding:gzip, deflate, sdch
    Accept-Language:en-US,en;q=0.8
    Cache-Control:max-age=0
    Proxy-Connection:keep-alive
    Upgrade-Insecure-Requests:1
    User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36
'''
def downloadGoogle(url, temp_folder, film_name_en, filmId):
    film_folder = '%s%s' % (temp_folder, film_name_en)
    os.mkdir(film_folder)
    local_filename = '%s/%s' % (film_folder, filmId)
    try:
        r = requests.get(url, stream=True)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    #f.flush() commented by recommendation from J.F.Sebastian
        return local_filename
    except Exception as e:
        print str(e)

temp_folder = '/home/hadn/film/'
# create connect mongo database
client = MongoClient()
# database films is selected
db = client["films"]

film = db.films.find_one({"film_type" : "series"})
filmId = film["crawler_film_id"]
link_crawler = film["crawler_link"]
film_name_en = film['film_name_en']

# create requests session & cookies
session = requests.session()
session.headers.update({'User-Agent': DEFAULT_USER_AGENTS[0]})
session.headers.update({'Accept-Encoding' : 'gzip, deflate, sdch'})
session.headers.update({'Accept-Language': 'en-US,en;q=0.8'})

url = 'http://hdonline.vn/phim-freshwater-ho-quai-thu-12358.html'
html_content = session.get(url)

file_html = '%s%s' % (temp_folder, 'output.txt')
with open(file_html, 'wb') as f:
    f.write(html_content.text.encode('utf-8'))

# save all html content into file
# run php cli to get token key
cmd = "php get-token.php %s" % (file_html)
cmd = shlex.split(cmd)
up = Popen(cmd, stdout=PIPE)
# get token key
token = up.stdout.readlines()[-1].split('"')[1]

# update headers Referer, X-Requested-With
session.headers.update({'Referer': url})
session.headers.update({'Connection' : 'keep-alive'})
session.headers.update({'X-Requested-With': 'XMLHttpRequest'})
session.headers.update({'Keep-Alive': 300})
session.headers.update({'Accept' : 'application/json, text/javascript, */*; q=0.01'})

# link to get detail film for downloading file mp4/m3u8
url_link = 'http://hdonline.vn/frontend/episode/xmlplay?ep=1&fid=12358&token=%s&_x=0.875115562264676&format=json' % token

# get link download
temp = session.get(url_link)
# get highest profiles of film
for i in temp.json()['level']:
    link, label = i.items()
    if len(temp.json()['level']) == 3:
        if label[1] == '720p'.decode('utf-8'):
            break
    else:
        if label[1] == '480p'.decode('utf-8'):
            break

# link download file
print link[1]
downloadGoogle(link[1], temp_folder, film_name_en, filmId)
