from bz2 import compress
import os
from PIL import Image
import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt
from skimage import data, img_as_float, color, io

import mlflow


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--image_folder", type=str)
parser.add_argument("--output_folder", type=str)
parser.add_argument("--new_size_ratio", type=float, default=0.9)
parser.add_argument("--width", type=int, default=64)
parser.add_argument("--height", type=int, default=64)

args = parser.parse_args()


def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"
    
def compress_img(image_path, image_name, output_path, new_size_ratio=0.9, quality=90, width=None, height=None, to_jpg=True):
    # load the image to memory
    img = Image.open(image_path)
    image_size = os.path.getsize(image_path)
    # print the size before compression/resizing
    print("[*] Size before compression:", get_size_format(image_size))
    if new_size_ratio < 1.0:
        # if resizing ratio is below 1.0, then multiply width & height with this ratio to reduce image size
        img = img.resize((int(img.size[0] * new_size_ratio), int(img.size[1] * new_size_ratio)), Image.ANTIALIAS)
    elif width and height:
        # if width and height are set, resize with them instead
        img = img.resize((width, height), Image.ANTIALIAS)
    filename, ext = os.path.splitext(image_name)
    if to_jpg:
        new_filename = f"{filename}_compressed.jpg"
    else:
        new_filename = f"{filename}_compressed{ext}"
    try:
        # save the image with the corresponding quality and optimize set to True
        output_file_path = os.path.join(output_path, new_filename)
        img.save(output_file_path, quality=quality, optimize=True)
    except OSError:
        # convert the image to RGB mode first
        img = img.convert("RGB")
        output_file_path = os.path.join(output_path, new_filename)
        img.save(output_file_path, quality=quality, optimize=True)
    new_image_size = os.path.getsize(output_file_path)
    print("[+] Size after compression:", get_size_format(new_image_size))
    mlflow.log_metric('size',new_image_size)


def main(args):
    images = os.listdir(args.image_folder)
    for image in images:
        image_path = os.path.join(args.image_folder, image)
        compress_img(image_path,image,args.output_folder, new_size_ratio=args.new_size_ratio, width=args.width, height=args.height)


if __name__ == "__main__":
    main(args)