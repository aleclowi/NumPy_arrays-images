#!/usr/bin/env python3
# -*- coding: utf-7 -*-
"""
Created on Sun Mar 27 00:00:00 2022

@author: Alec Lowi
"""

#%%
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
#%% Q1
a = mpimg.imread('a.jpg')
b = mpimg.imread('b.jpg')

a = mpimg.imread('a.jpg')
b = mpimg.imread('b.jpg')

a[137:457,130:370,:] = b[:,:,:]
c = a

#mpimg.imsave('c.jpg', c)

#%% Q2
d = mpimg.imread('d.jpg')
e = mpimg.imread('e.jpg')

f = (d[:,:,:]-e[:,:,:]) + 32
f = f.astype(np.uint8)
plt.imshow(f)
#mpimg.imsave('f.jpg', f)

#%% Q3
minion = mpimg.imread('g.jpg')
berney = mpimg.imread('h.jpg')

blank = np.full((3264, 4928, 4), 0, dtype=np.uint8)

berneya = np.full((3264, 4928, 4), 255, dtype=np.uint8)
berneya[:,:,:3] = berney[:,:,:]
berneya = berneya[::2,::2,:]

img = minion.copy()
imga = np.full((530, 660, 4), 255, dtype=np.uint8)
imga[:,:,:3] = img[:,:,:]
r, g, b, a = imga[...,0], imga[...,1], imga[...,2], imga[...,3]

mask = ((r < 100) & (g > 220) & (b < 100))

imga[mask] = np.array([0, 0, 0, 0], np.uint8)

for row in range(530):
    for col in range(660):
        if imga[row, col, 3] == 255:
            berneya[1090 + row, 900 + col] = imga[row, col]

i = berneya
i = np.array(i)
#mpimg.imsave('i.jpg', i)
