#! python3
# DownloadXkcd.py - Downloads all Xkcd comics

import requests
import os
import bs4

url = 'http://xkcd.com'
os.makedirs('C:\\xkcd', exist_ok=True)
while not url.endswith('#'):
    # Download the page.
    print('Downloading the webpage')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    # Find the URL of the comic image.
    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print('Could not find the image')
    else:
        comic_url = 'http:' + comic_elem[0].get('src')
        # Download the image.
        print('Downloading image %s…' % (comic_url))
        res = requests.get(comic_url)
        res.raise_for_status()
        # Save the image to ./xkcd.
        image_file = open(os.path.join('C:\\xkcd', os.path.basename(comic_url)), 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

    # Get the Prev button's url.
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')

print('Done!')
