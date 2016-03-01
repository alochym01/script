#!/usr/bin/python

import httplib
import httplib2
import os
import random
import sys
import time

from apiclient.discovery import build
from apiclient.errors import HttpError
from apiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow


# Explicitly tell the underlying HTTP transport library not to retry, since
# we are handling retry logic ourselves.
httplib2.RETRIES = 1

# Maximum number of times to retry before giving up.
MAX_RETRIES = 10

# Always retry when these exceptions are raised.
RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError, httplib.NotConnected,
  httplib.IncompleteRead, httplib.ImproperConnectionState,
  httplib.CannotSendRequest, httplib.CannotSendHeader,
  httplib.ResponseNotReady, httplib.BadStatusLine)

# Always retry when an apiclient.errors.HttpError with one of these status
# codes is raised.
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the Google Developers Console at
# https://console.developers.google.com/.
# Please ensure that you have enabled the YouTube Data API for your project.
# For more information about using OAuth2 to access the YouTube Data API, see:
#   https://developers.google.com/youtube/v3/guides/authentication
# For more information about the client_secrets.json file format, see:
#   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
CLIENT_SECRETS_FILE = "/home/hadn/Downloads/adsense/wowebookpro/client_secret.json"

# This OAuth 2.0 access scope allows an application to upload files to the
# authenticated user's YouTube channel, but doesn't allow other types of access.
YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# This variable defines a message to display if the CLIENT_SECRETS_FILE is
# missing.
MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

   %s

with information from the Developers Console
https://console.developers.google.com/

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   CLIENT_SECRETS_FILE))

VALID_PRIVACY_STATUSES = ("public", "private", "unlisted")


def get_authenticated_service(args):
  flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
    scope=YOUTUBE_UPLOAD_SCOPE,
    message=MISSING_CLIENT_SECRETS_MESSAGE)

  storage = Storage("/home/hadn/Downloads/adsense/wowebookpro/youtube-oauth2.json")
  credentials = storage.get()

  if credentials is None or credentials.invalid:
    credentials = run_flow(flow, storage, args)

  return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    http=credentials.authorize(httplib2.Http()))

def add_video_to_playlist(youtube,videoID,playlistID):
	add_video_request=youtube.playlistItems().insert(
		part="snippet",
		body={
		    'snippet': {
		      'playlistId': playlistID,
		      'resourceId': {
		        'kind': 'youtube#video',
			'videoId': videoID
		      }
		    }
		}
	).execute()


if __name__ == '__main__':
  argparser.add_argument("--videoId", help="Video file to upload")
  argparser.add_argument("--playlistId", help="playlist ID")
  args = argparser.parse_args()
  youtube = get_authenticated_service(args)
  playlist = {'cong-nghe': 'PLiYWpBi4dlS9FDavsIanMMCHbKEkv5D0k','san-pham': 'PLiYWpBi4dlS9FDavsIanMMCHbKEkv5D0k','bat-dong-san': 'PLiYWpBi4dlS8XYlNQdY8jT7o-F7Fv_VOH','suc-khoe': 'PLiYWpBi4dlS-199bV_GJIY3oECuBbnh5t','du-lich': 'PLiYWpBi4dlS-199bV_GJIY3oECuBbnh5t','the-gioi-do-day': 'PLiYWpBi4dlS-199bV_GJIY3oECuBbnh5t','phap-luat': 'PLiYWpBi4dlS86fQs8kN4llHAzLfds-tsl','tu-van': 'PLiYWpBi4dlS86fQs8kN4llHAzLfds-tsl','doi-song': 'PLiYWpBi4dlS8QZgQFQBBQkZkcUU9wwm5j','chinh-tri': 'PLiYWpBi4dlS8QZgQFQBBQkZkcUU9wwm5j','xa-hoi': 'PLiYWpBi4dlS8QZgQFQBBQkZkcUU9wwm5j','thi-truong': 'PLiYWpBi4dlS_pglumTBr81Ri61d3YiXgt','kinh-te': 'PLiYWpBi4dlS_pglumTBr81Ri61d3YiXgt','giao-duc': 'PLiYWpBi4dlS8QD8DGdJgSVYHXLMK1D8Pe','moi-ngay-mot-cuon-sach': 'PLiYWpBi4dlS8QD8DGdJgSVYHXLMK1D8Pe','tam-long-viet': 'PLiYWpBi4dlS8QD8DGdJgSVYHXLMK1D8Pe','cuoc-song-thuong-ngay': 'PLiYWpBi4dlS8QD8DGdJgSVYHXLMK1D8Pe','cac-mon-khac': 'PLiYWpBi4dlS9njCqjrSqVDz8uBi8SIa05','bong-da': 'PLiYWpBi4dlS9njCqjrSqVDz8uBi8SIa05','the-thao': 'PLiYWpBi4dlS9njCqjrSqVDz8uBi8SIa05','viet-nam-va-the-gioi': 'PLiYWpBi4dlS8QZgQFQBBQkZkcUU9wwm5j','van-de-hom-nay': 'PLiYWpBi4dlS8QZgQFQBBQkZkcUU9wwm5j','trong-nuoc': 'PLiYWpBi4dlS8QZgQFQBBQkZkcUU9wwm5j','tin-tuc': 'PLiYWpBi4dlS8QZgQFQBBQkZkcUU9wwm5j','the-gioi': 'PLiYWpBi4dlS8QZgQFQBBQkZkcUU9wwm5j','chuyen-dong-24h': 'PLiYWpBi4dlS8QZgQFQBBQkZkcUU9wwm5j','van-hoa-giai-tri':'PLiYWpBi4dlS_pglumTBr81Ri61d3YiXgt', 'tai-chinh':'PLiYWpBi4dlS_pglumTBr81Ri61d3YiXgt', 'toan-canh-the-gioi': 'PLiYWpBi4dlS8QZgQFQBBQkZkcUU9wwm5j', 'gioi-tinh': 'PLiYWpBi4dlS86fQs8kN4llHAzLfds-tsl', 'ben-le': 'PLiYWpBi4dlS8QZgQFQBBQkZkcUU9wwm5j', 'dang-trong-cuoc-song-hom-nay': 'PLiYWpBi4dlS8QZgQFQBBQkZkcUU9wwm5j', 'su-kien-va-binh-luan': 'PLiYWpBi4dlS8QZgQFQBBQkZkcUU9wwm5j', 'dan-hoi-bo-truong-tra-loi': 'PLiYWpBi4dlS8QZgQFQBBQkZkcUU9wwm5j', 'truyen-hinh':'PLiYWpBi4dlS8Fy8qA81aO7kQjP4L0IjiC', 'goc-khan-gia':'PLiYWpBi4dlS-199bV_GJIY3oECuBbnh5t'}
  try:
    add_video_to_playlist(youtube, args.videoId, "PLiYWpBi4dlS-BvSE7gVw5U4_9XDL94FKT")
    add_video_to_playlist(youtube, args.videoId, playlist[args.playlistId])
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
