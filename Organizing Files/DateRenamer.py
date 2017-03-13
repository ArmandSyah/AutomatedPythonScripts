#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil, re, os

# Create a regex that matches files with the American date format.
date_pattern = re.compile(r"""^(.*?)
                          ((0|1)?\d)-
                          ((0|1|2|3)?\d)-
                          ((19|20)\d\d)
                          (.*?)$
                          """, re.VERBOSE)

# Loop over the files in the working directory.
for american_filename in os.listdir('.'):
    matching_object = date_pattern.search(american_filename)

    # Skip files without a date.
    if matching_object == None:
        continue

    # Get the different parts of the filename.
    before_part = matching_object.group(1)
    month_part = matching_object.group(2)
    day_part = matching_object.group(4)
    year_part = matching_object.group(6)
    after_part = matching_object.group(8)

    # Form the European-style filename.
    euro_filename = before_part + day_part + '-' + month_part + '-' + year_part + after_part

    # Get the full, absolute file paths.
    abs_working_directory = os.path.abspath('.')
    american_filename = os.path.join(abs_working_directory, american_filename)
    euro_filename = os.path.join(abs_working_directory, euro_filename)

    # Rename the files.
    print('Renaming "%s" to "%s" ...' % (american_filename, euro_filename))
    shutil.move(american_filename, euro_filename)