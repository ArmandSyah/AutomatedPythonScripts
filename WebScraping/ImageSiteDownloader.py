#! python3
# ImageSiteDownloader.py - downloads images of a specific category from Imgur

import requests
import os
import bs4
import sys
from time import time

# Make the folder where all images are saved
os.makedirs('C:\\ImageFolder', exist_ok=True)
# Get User's search query

print('What would you like to search for?')
search = str(input())
search = search.split(" ")
while len(search) < 1:
    print('Please input at least 1 word')
    search = str(input())
    search = search.split(" ")

#  Make an HTTPRequest to users search query
if len(search) == 1:
    url = 'https://www.imgur.com/search/?q={}'.format(search[0])
else:
    url = 'https://www.imgur.com/search/?q={}'.format(search[0])
    for i in range(1, len(search)):
        url += '+{}'.format(search[i])

print(url)

res = ""
while res == "":
    try:
        res = requests.get(url)
        res.raise_for_status()
    except requests.exceptions.ConnectionError:
        print('Connection Refused')
        time.sleep(10)

soup = bs4.BeautifulSoup(res.text, "html.parser")

img_elems = soup.select('img')
if len(img_elems) == 0:
    print('Could not find images')
    sys.exit(0)

# Pilfer through the images and save into folder
for i in range(50):
    image_url = img_elems[i].get('src')
    image_url = 'http://' + image_url[2:]
    img = requests.get(image_url)
    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError:
        print("failed image download")
        continue
    image_file = open(os.path.join('C:\\ImageFolder', os.path.basename(image_url)), 'wb')
    for chunk in res.iter_content(1000000):
        image_file.write(chunk)
    image_file.close()
    print('Finished downloading pic {}'.format(i))

print('Finished downloading pics')
sys.exit(0)

