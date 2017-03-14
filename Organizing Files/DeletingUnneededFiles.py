#! python3
# DeletingUnneededFiles.py - Shows a list of files in folders of size more than 100mb

import os


def checkfolder(folder):
    source_folder = os.path.abspath(folder)

    for foldername, subfolders, filenames in os.walk(source_folder):
        if os.path.getsize(foldername) > 1000000:
            print('folder: ' + os.path.abspath(foldername))
        for filename in filenames:
            if os.path.getsize(os.path.join(foldername, filename)) > 100000000:
                print('file: ' + os.path.abspath(filename))

checkfolder('C:\\Users\\Armand Syahtama\\')
