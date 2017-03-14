#! python3
# SelectiveCopy.py - Copies PDFs or JPGs into another folder

import os
import shutil
# import logging
# logging.basicConfig(level=logging.DEBUG, format= ' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug('Start of the program')



def selectcopy(source_folder, dest_folder, extension):
    source_folder = os.path.abspath(source_folder)
    dest_folder = os.path.abspath(dest_folder)

    print(source_folder)
    print(dest_folder)

    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            # logging.debug('File: ' + filename)
            if filename.endswith('.' + extension):
                print(filename)
                shutil.copy(os.path.join(foldername, filename), dest_folder)

selectcopy('C:\\Users\\Armand Syahtama\\Dropbox\\Resume shit', 'D:\\Stuff', 'pdf')
# logging.debug('End of Program')
