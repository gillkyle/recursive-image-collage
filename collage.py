#!/usr/bin/env python3
import argparse
import os
from PIL import Image               # pip3 install pillow
from foldersearch import find_images
import math


THUMBNAILS_PER_ROW = 4
THUMBNAIL_WIDTH = 200
THUMBNAIL_HEIGHT = 200


########################
# Main program

def main(args):
    '''
    Creates a collage by recursively finding images in a directory path.
    '''
    # find the images
    imgpaths = []
    for filepath in find_images(os.path.abspath(args.searchpath)):
        imgpaths.append(filepath)
    if len(imgpaths) == 0:
        print('No images found')
        return

    num_rows = math.ceil(len(imgpaths) / THUMBNAILS_PER_ROW)
    img_size = (THUMBNAILS_PER_ROW * THUMBNAIL_WIDTH,
                num_rows * THUMBNAIL_HEIGHT)
    # create a new, RGB image
    collage = Image.new('RGB', img_size)

    x = 0
    y = 0
    # place the thumbnails
    for imgnum, imgpath in enumerate(imgpaths):
        paste_position = (THUMBNAIL_WIDTH * x, THUMBNAIL_HEIGHT * y)
        # open the image and convert to RGB
        im = Image.open(imgpath)
        im.convert('RGB')
        # resize to a thumbnail
        im.thumbnail((THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT))
        # paste in next position
        collage.paste(im, paste_position)
        # if next image would the 5th on this row, move down a row
        if (imgnum + 1) % 4 == 0:
            x = 0
            y += 1
        else:
            x += 1

    # save the image
    print(f'Writing {args.collage}')
    collage.save(args.collage)


########################
# Bootstrap
parser = argparse.ArgumentParser(
    description='Creates a collage by recursively finding images in a directory path')
parser.add_argument('collage', help='file name to write the collage to')
parser.add_argument('searchpath', help='directory path to start searching')
args = parser.parse_args()
main(args)
