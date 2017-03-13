#! python3
# SelectiveCopy.py - Copies PDFs or JPGs into another folder

import os, shutil

def selectCopy(source_folder, dest_folder, extension):
    source_folder = os.path.abspath(source_folder)
    dest_folder = os.path.abspath(dest_folder)

    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.endswith('.' + extension):
                shutil.copy(filename, dest_folder)