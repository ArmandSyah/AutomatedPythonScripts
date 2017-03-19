#! python3
# MultidownloadXkcd.py - Downloads XKCD comics using multiple threads.

import requests
import os
import bs4
import threading

os.makedirs('xkcd', exist_ok=True)


def downloadxkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        # Download the page
        print('Downloading page http://xkcd.com/%s…' % url_number)
        res = requests.get('http://xkcd.com/%s' % url_number)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text)

        # Find the URL of the comic image.
        comic_elem = soup.select('#comic img')
        if not comic_elem:
            print('Could not find comic image')
        else:
            comic_url = 'http:' + comic_elem[0].get('src')
            # Download the image
            print('Downloading image %s…' % comic_url)
            res = requests.get(comic_url)
            res.raise_for_status()

            # Save the image to ./xkcd.
            image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

# Create and start Thread objects
download_threads = []
for i in range(0, 1400, 100):
    download_thread = threading.Thread(target=downloadxkcd, args=(i, i + 99))
    download_threads.append(download_thread)
    download_thread.start()
# Wait for all threads to end
for download_thread in download_threads:
    download_thread.join()

print('Done.')
