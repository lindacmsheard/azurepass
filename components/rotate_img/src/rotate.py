#import cv2 and imutils module
#import cv2  
#import imutils
from PIL import Image


import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("--image_folder", type=str)
parser.add_argument("--degrees", type=int)
parser.add_argument("--output_folder", type=str)

args = parser.parse_args()

print("sample_input_string: %s" % args.image_folder)
print("rotation:", args.degrees)
print("sample_output_data path: %s" % args.output_folder)

print("files in input_data path: ")
arr = os.listdir(args.image_folder)
print(arr)

for filename in arr:
    print("rotating file: %s ..." % filename)
    # with open(os.path.join(args.input_data, filename), "r") as handle:
    #     print(handle.read())

    # read an image as input using OpenCV
    #input_image = cv2.imread(os.path.join(args.input_data, filename))
    #output_image = imutils.rotate(input_image, angle=90)
    #cv2.imwrite(os.path.join(args.output_folder, "rotated90_%s" % filename), output_image)

    # read image with Pillow
    input_image = Image.open(os.path.join(args.image_folder, filename))
    output_image = input_image.rotate(args.degrees)
    output_image.save(os.path.join(args.output_folder, "rotated%s_%s" % (str(args.degrees),filename)))

 