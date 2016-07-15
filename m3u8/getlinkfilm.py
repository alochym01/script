from subprocess import Popen, PIPE
import shlex
from pymongo import MongoClient
import json
import re

# create connect mongo database
client = MongoClient()
# database films is selected
db = client["films"]

film = db.films.find_one({"crawler_film_id" : 12351})
filmId = film["crawler_film_id"]
link_crawler = film["crawler_link"]
film_name_en = re.sub(' ', '_', film['film_name_en'])

#temp_folder = '/home/hadn/Laravel/film/cli/database/alofilm_db/alofilm/m3u8'
# how to get the episode of the film - default is 1
episode_number = 1
# film filename
# fileName = '%s-%s' % (filmId, episode_number)
# repare directory for saving film
temp_folder = '/home/hadn/film/'
film_folder = '%s%s/' % (temp_folder, film_name_en)

# save all html content into file
# run php cli to get all info of film - check film_sample.txt
# if know the javascript we can execute by execjs in python
cmd = "php get-link.php %s %s" % (filmId, episode_number)
cmd = shlex.split(cmd)
up = Popen(cmd, stdout=PIPE)

# get results json string from php script
stddata = up.communicate()

# load info film into python object
linkInfo = json.loads(stddata[0])

try:
    # link film
    lastLabelFilm = linkInfo['level'][-1]['file']
    # starting download film from google
    # using: python google_download.py link_film film_folder film_name
    cmd = '/home/hadn/python/bin/python google_download.py "%s" "%s" "%s" "%s" "%s"' % (lastLabelFilm, film_folder, filmId, film_name_en, episode_number)
    google_cmd = shlex.split(cmd)
    Popen(google_cmd, stdout=PIPE)
except:
    # using: python m3u8_download.py link_crawler folder filmId film_folder episode_number
    cmd = '/home/hadn/python/bin/python m3u8_download.py "%s" "%s" "%s" "%s" "%s"' % (link_crawler, film_folder, filmId, film_name_en, episode_number)
    m3u8_cmd = shlex.split(cmd)
    print cmd
    Popen(m3u8_cmd, stdout=PIPE)
