#!/usr/bin/python3

# Python3 script for converting tiff images to JPEG

from PIL import Image
import os

imgs_dir = "images"
files = os.listdir(imgs_dir)

for img_file in files:
    img_path = os.path.join(imgs_dir, img_file)
    if os.path.isfile(img_path):
        old_img = Image.open(img_path)
        new_img = old_img.rotate(90).resize((128,128)).convert('RGB')
        outfile_name = img_file + ".jpg"
        new_img.save(outfile_name, "JPEG", quality=90)



