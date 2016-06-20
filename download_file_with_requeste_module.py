#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

temp_path = '/home/hadn/phim.mp4'
url = 'https://lh3.googleusercontent.com/I13hZ5yM2uUMK9SIdcym76LRZ2B8isRzpVR27bdnBg9_dAGlQeTtt4s6sStQOW8Y9UXKgYgvNQ=m18?itag=18&type=video/mp4'
# download img link > 1G store from website and save as temp_path
with open(temp_path, 'wb') as handle:
    response = requests.get(url, stream=True)
    if not response.ok:
        print (error)
    for block in response.iter_content(1024):
        handle.write(block)
