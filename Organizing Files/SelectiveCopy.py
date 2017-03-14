#! python3
# SelectiveCopy.py - Copies PDFs or JPGs into another folder

import os
import shutil


def selectcopy(source_folder, dest_folder, extension):
    source_folder = os.path.abspath(source_folder)
    dest_folder = os.path.abspath(dest_folder)

    print(source_folder)
    print(dest_folder)

    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.endswith('.' + extension):
                print(filename)
                shutil.copy(os.path.join(foldername, filename), dest_folder)

selectcopy('C:\\', 'D:\\Stuff', 'pdf')
