# -*- coding: utf-8 -*-
"""FilterEffects.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K5qLzMLr-LA3DcbqmJeF6Ilrmm6YnLxO

# Libraries
"""

#link = https://colab.research.google.com/drive/1K5qLzMLr-LA3DcbqmJeF6Ilrmm6YnLxO?usp=sharing
# Necessary imports
import cv2 as cv
import cv2
import numpy as np
from google.colab.patches import cv2_imshow

from google.colab import drive
drive.mount('/content/drive')

"""# Blur Effect"""

img1 = cv2.imread('abc.jpeg',0)  # 0 means greyscale image
cv2_imshow(img1)

# Filters - first (2,2), second(4,4), third(6,6), last(8,8)
blurred_1 = np.hstack([
  cv2.blur(img1,(2,2)),
  cv2.blur(img1,(4,4)),
  cv2.blur(img1,(6,6)),
  cv2.blur(img1,(8,8))])
cv2_imshow(blurred_1)

"""# Sharpen filter"""

sharpen_filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
sharpen_img_1=cv2.filter2D(img1,-1,sharpen_filter)
cv2_imshow(img1)
cv2_imshow(sharpen_img_1)

"""# Vintage Color filter"""

img2 = cv2.imread('abc.jpeg') 
(b,g,r)=cv2.split(img2)
r_new = r*1.8 + g*1 + b*1
g_new = r*1 + g*1.4 + b*1
b_new = r*1. + g*1 + b*0.32
img_new=cv2.merge([b_new, g_new, r_new])
cv2_imshow(img2)
cv2_imshow(img_new)

"""# Painting filter

"""

img3 = cv2.imread('abc.jpeg') 
dst_gray, dst_color = cv2.pencilSketch(img3, sigma_s=80, sigma_r=0.1, shade_factor=0.02) 
# s = size of the neighborhood
# r = ?
# shade = image intensity

cv2_imshow(dst_gray)
cv2_imshow(dst_color)

"""# Brightness filter

"""

img4 = cv2.imread('abc.jpeg') 
cv2_imshow(img4)

brightness_value=3   
contrast_value=50  

result =cv2.addWeighted(img4,brightness_value,np.zeros(img4.shape,img4.dtype),0,contrast_value)
cv2_imshow(result)

"""# Blue Grain effect


"""

img4 = cv2.imread('abc.jpeg') 

im4 = np.zeros(img4.shape, np.uint8) 
min = 0
max = 100
cv2.randn(im4,min,max) # random num
grain = cv2.add(img4, im4) #adding noise
cv2_imshow(img4)
cv2_imshow(grain)