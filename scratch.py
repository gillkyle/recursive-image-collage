import os
import fnmatch
from PIL import Image


def is_image(filename):
    # TODO fix this using fnmatch to match globs of *.png
    return True


def find_images(dirpath):
    for filename in os.listdir(dirpath):
        # if a directory find_images(os.path.join(dirpath, filename))
        fullpath = os.path.join(dirpath, filename)
        if os.path.isdir(fullpath):
            yield from find_images(fullpath)
        # else if a*.png yield it
        elif is_image(fullpath):
            print('>>>>>>', fullpath)
            yield fullpath


for path in find_images("img"):
    print(path)
