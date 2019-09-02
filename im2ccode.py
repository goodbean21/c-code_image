# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:03:29 2019

@author: Soluciones Kenko
"""

from argparse import ArgumentParser
from os.path import realpath

import cv2
#import numpy as np
#import skimage as ski

args = ArgumentParser("im2ccode")
args.add_argument("--im", help = "PATH de la imagen a convertir.", metavar = "IMFILE")

args.add_argument("--height", help = "HEIGHT de la imagen.",
                  default = -1, type = int, metavar="HEIGHT")
args.add_argument("--width", help = "WIDTH de la imagen.", default = -1, type = int, metavar = "WIDTH")
args = args.parse_args()

def reshape(im):
    if args.height == -1:
        height = im.shape[0]
        
    else:
        height = args.height
    
    
    if args.width == -1:
        width = im.shape[1]
        
    else:
        width = args.width

    return cv2.resize(im, (width, height))

def display_image(im):
    cv2.imshow(image_name, im)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
def get_size(im):
    print("The size of the image is: {} x {}".format(im.shape[0], image.shape[1]))
    
if __name__ == "__main__":
    image_path = realpath(args.im)
    image_name = args.im.split('.')[0]
    bmp_path = image_name + ".bmp"
    
    image = cv2.imread(image_path)
    image = reshape(image)
    get_size(image)
    
    cv2.imwrite(bmp_path, image)
    display_image(cv2.imread(realpath(bmp_path)))
