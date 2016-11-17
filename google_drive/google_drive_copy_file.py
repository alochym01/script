#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.tools import argparser

# try:
#     import argparse
#     flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
# except ImportError:
#     flags = None
flags = None

SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = '/home/hadn/hang.cucku/client_secret.json'
APPLICATION_NAME = 'Drive API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    #home_dir = os.path.expanduser('~')
    #credential_dir = os.path.join(home_dir, '.credentials')
    #if not os.path.exists(credential_dir):
    #    os.makedirs(credential_dir)
    #credential_path = os.path.join(credential_dir,
                                   #'drive-python-quickstart.json')

    store = Storage('/home/hadn/hang.cucku/drive-python-quickstart.json')
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        #print('Storing credentials to ' + credential_path)
    return credentials

def main(args):
    """Shows basic usage of the Google Drive API.

    Creates a Google Drive API service object and outputs the names and IDs
    for up to 10 files.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    # account hang.cucku with folder name is films
    folder_id = '0B2ffjUvb0vY0dlZ5U3RCbVA1dDQ'
    folder_id = args.folderid
    file_id = args.fileid
    file_metadata = {
        #'name' : 'photo.jpg',
        'name' : args.name,
        'parents': [ folder_id ]
    }
    # print(file_id)
    # print(file_metadata)
    results = service.files().copy(fileId=file_id, body=file_metadata).execute()

    print('{0}'.format(results.get('id')))

if __name__ == '__main__':
    argparser.add_argument("--fileid", required=True, help="Video file to upload")
    argparser.add_argument("--folderid", required=True, help="Video file to upload")
    argparser.add_argument("--name", required=True, help="Video title")

    args = argparser.parse_args()
    main(args)
