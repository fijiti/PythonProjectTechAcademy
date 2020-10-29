
# FILE TRANSFER ASSIGNMENT PART TWO

import time
import shutil
import os

# Variable for reference to seconds in a day
SECONDS_IN_DAY = 24 * 60 * 60

# Set where source files are
source = 'createModFolder/'
# Set destination path for files
destination = 'destinationFolder/'
files = os.listdir(source)

now = time.time()
before = now - SECONDS_IN_DAY

def last_mod_time(fname):
    return os.path.getmtime(fname)



for fname in files:
    src_fname = os.path.join(source, fname)
    if last_mod_time(src_fname) < before:
        dst_fname = os.path.join(destination, fname)
        shutil.move(src_fname, dst_fname)
