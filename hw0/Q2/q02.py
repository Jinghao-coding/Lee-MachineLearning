# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:32:07 2019

@author: JingHao
"""
from __future__ import print_function
from PIL import Image


img1 = Image.open("data/lena.png")
img2 = Image.open("data/lena_modified.png")

#print(img1.size, img1.format, img1.mode)

w, h = img2.size

for j in range(h):
    for i in range(w):
        if img1.getpixel((i, j)) == img2.getpixel((i, j)):
            img2.putpixel((i, j), 255)
            
img2.save("ans_two.png")