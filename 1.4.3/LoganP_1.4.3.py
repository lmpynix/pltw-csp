# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 12:17:32 2017

@author: 156048
"""

import matplotlib.pyplot as plt
import numpy as np
import math

IMG_NAME = "woman.jpg"

def stepFive():
    fig, ax = plt.subplots(1)
    img = plt.imread(IMG_NAME)
    # This line is needed to make the img array writeable.
    img.flags.writeable = True
    for row in range(420, 475):
        for column in range(125, 175):
            img[row][column] = [0, 255, 0] # red + green = yellow
    ax.imshow(img)

def stepSix():
    fig, ax = plt.subplots(1)
    img = plt.imread(IMG_NAME)
  
     # This line is needed to make the img array writeable.
    img.flags.writeable = True
    
    width = len(img[0])
    for r in range(150):
        for c in range(width):
            if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
                img[r][c]=[(127 * (math.cos(0.05 * c) + 1)),0,(127 * (math.sin(0.1 * c + 10) + 1))] # R + B = magenta
    ax.imshow(img)
    # 8a. Iterate over all of the pixels in the image.  If the pixel's brightness value exceeds a certain amount, change its value.
    
def stepSixB():
    fig, ax = plt.subplots(1)
    img = plt.imread(IMG_NAME)
  
     # This line is needed to make the img array writeable.
    img.flags.writeable = True
    
    for r in range(420, 475):
        for c in range(125, 175):
            if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
                img[r][c]=[255,0,(127 * (math.sin(0.1 * c + 10) + 1))] # R + B = magenta
    ax.imshow(img)