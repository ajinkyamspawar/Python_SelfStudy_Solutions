# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 18:25:41 2023

@author: AJINKYA
"""

import PIL 
from PIL import Image 

img = PIL.Image.open("D:/1_AJINKYA_PAWAR/3_SOFTWARE JOB/1_CDAC/2_KNOW-IT/Photos/SAVE_20221122_214911.jpg")

width, height = img.size

print(width,"X",height)

