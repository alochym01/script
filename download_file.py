import requests

# download img from website and save as temp_path
with open(temp_path, 'wb') as handle:
    response = requests.get(img, stream=True)
    if not response.ok:
        print "error"
    for block in response.iter_content(1024):
        handle.write(block)

