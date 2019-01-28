#!/usr/bin/env python3
import os
from fnmatch import fnmatch


IMAGE_GLOBS = {
    '*.png',
    '*.jpg',
}


def is_image(filename):
    '''
    Returns True if the given filename matches one of the IMAGE_GLOBS patterns.
    Just check the filename itself (don't inspect the file contents).
    '''
    for glob in IMAGE_GLOBS:
        if fnmatch(filename, glob):
            return True


def find_images(rootpath, subpath=''):
    '''
    Generator function that returns the images in the given directory
    tree (includes subdirectories). The returned image paths are relative to
    the given path.

    Use os.listdir() to get the files in the current directory (don't use os.walk
    or glob.glob).
    '''
    for filename in os.listdir(rootpath):
        print(filename)
        # if a directory find_images(os.path.join(rootpath, filename))
        fullpath = os.path.join(rootpath, filename)
        if os.path.isdir(fullpath):
            yield from find_images(fullpath)
        # else if a*.png yield it
        elif is_image(fullpath):
            print('>>>>>>', fullpath)
            yield fullpath


# print(is_image('asdf.jpg'))
# print(is_image('asdf.png'))
for path in find_images("img"):
    print(path)
