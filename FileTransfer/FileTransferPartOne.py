
# FILE TRANSFER ASSIGNMENT PART ONE

import shutil
import os

# Set where the source of the files are
source = 'folderA/'

# Set the destination path to folder B
destination = 'folderB/'
files = os.listdir(source)

for i in files:
    # We are saying move the files represented by 'i' to there new destination
    shutil.move(source+i, destination)
