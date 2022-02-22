# Created by Shamik Karkhanis on May 22, 2020
# Edited on Feb 20, 2022

# imports
import time, os, shutil

# Removes all files from source directory and transfers to destination directory
def cleanup():

    # Specifies locations to transfer to and from
    source = '/Users/shamikkarkhanis/Desktop/'
    destination = '/Users/shamikkarkhanis/Documents/DF_DesktopFiles/'

    createDirectory(destination)

    # Stores names files from source directory in list
    source_files = os.listdir(source)

    # Copies all files from source directory then pastes them into destination directory
    for file in source_files:

        #copies file from source and adds to destination
        shutil.copy(source+file, destination+file)

        # Removes extra copies of original files in source directory
        os.remove(source+file)

# If destination directory does not exist it will make one
def createDirectory(direc):
    if not os.path.exists(direc):
        os.makedirs(direc)
    
# Runs cleanup() after a certain time repeatedly
def cleanup_time():

    # The brain behind the timer
    while True:
        cleanup()
        time.sleep(10)

# Starts the timer and cleanup process
cleanup_time()
