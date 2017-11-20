# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 12:46:41 2017

@author: 156048
"""

# Import vaious helpful things
import matplotlib.pyplot as plt
import numpy as np
import os.path as path
import math

# Constants
IMAGE_FILE_NAME = "woman.jpg"

# Make some of that sweet directory object
my_directory = path.dirname(path.abspath(__file__))
image_filename = my_directory + '\\' + IMAGE_FILE_NAME
img = plt.imread(image_filename)

# make me some plots
fig, axarr = plt.subplots(2, 2) 
#8a fig is an instance of numpy.Figure, axarr is an array of AxesSubplot objects.
axarr[0, 0].imshow(img, interpolation='none')
axarr[0, 0].set_title('Woman Images')
lum_img = img[:, :, 0]
axarr[0, 1].imshow(lum_img, interpolation='none', cmap='Greens_r')
axarr[1, 0].imshow(lum_img, interpolation='none', cmap='hot')
axarr[1, 1].imshow(lum_img, interpolation='none', cmap='gist_ncar')

# z = fig.show() # This would be necessary if not for my iPython placing the graphics inline.
# In line 22, the fig object is having its show method called.
# That method is being given 0 arguments, and the object is an instance of numpy.Figure
#8c. the comments explain the lines below them.

# Make dos WOmEnS
f2, ax2arr = plt.subplots(1, 2)
ax2arr[0].set_title("TwO WOmEnS")
for ax in ax2arr:
    ax.imshow(img)
#9a. In line 22, the fig object is having its show method called.

def make_many_fritzes(num):
    img = plt.imread("fritz.png")
    rowcol = math.ceil(math.sqrt(num))
    fig, axarr = plt.subplots(rowcol, rowcol)
    numtimes = 0
    for row in axarr:
        for cell in row:
            if numtimes < num:
                cell.imshow(img, interpolation='none')
            cell.set_axis_off()
            numtimes += 1

def zoomed_in_jc():
    img = plt.imread("JC.jpg")
    greenimg = img[:, :, 0]
    fig, axarr = plt.subplots(1, 3)
    for ax in axarr:
        ax.imshow(img, interpolation='none')
        ax.set_xlim(30, 85)
        ax.set_ylim(55, 0)
    axarr[0].set_title("Respecc")
    axarr[1].set_xlim(48, 58)
    axarr[1].set_ylim(38, 22)
    axarr[2].set_title("U CAN'T SEE ME")
    axarr[2].imshow(greenimg, cmap='Greens')
    axarr[2].set_xlim(55, 65)
    axarr[2].set_ylim(24.5, 20)
    