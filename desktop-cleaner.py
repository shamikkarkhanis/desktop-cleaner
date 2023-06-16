#!/usr/bin/env python
# Created by Shamik Karkhanis on May 22, 2020
# Edited on Feb 20, 2022
# Edited on June 15, 2022

# imports
import time, os, shutil

def createDirectory(direc):
    if not os.path.exists(direc):
        os.makedirs(direc)

# add respective directories here: 
source = ''
mediaDes = ''
imgDes = ''
ssDes = ''

createDirectory(mediaDes)
createDirectory(mediaDes)
createDirectory(imgDes)


def cleanup():

    # Stores names files from source directory in list
    source_files = os.listdir(source)

    # Copies all files from source directory then pastes them into destination directory
    for file in source_files:
        moveFiles(file)


# If destination directory does not exist it will make one

def moveFiles(file):
    fileExt = os.path.splitext(file)[1]
    fileName = os.path.splitext(file)[0]

    mediaExt = ['.mp4', '.mp3', '.ma4', '.mov']
    imgExt = ['.jpeg', '.png', '.jpg']

    if fileExt in mediaExt:
        shutil.copy(source + file, mediaDes + file)
    elif 'Screenshot' in fileName:
        shutil.copy(source + file, ssDes + file)
    elif fileExt.lower() in imgExt:
        shutil.copy(source + file, imgDes + file)

    os.remove(source+file)

# Runs cleanup() after a certain time repeatedly
cleanup()
