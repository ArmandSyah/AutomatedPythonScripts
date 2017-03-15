#! python3
# MapIt.py - launches google maps in the browser using address from command line or clipboard

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
