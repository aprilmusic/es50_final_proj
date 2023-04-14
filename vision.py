# Import required libraries
from PIL import Image
import numpy as np
# from skimage import io
import matplotlib.pyplot as plt
import cv2

background = cv2.imread('images/science_center1680972200.069715.png')
twotrucks = cv2.imread('images/science_center1680284125.821405.png')
print(background.shape)

img = cv2.imread('images/science_center1680972203.6774762.png')
img2 = cv2.imread('images/science_center1680972207.511832.png')
# io.imshow(background[:, :, 3])
# io.imshow(img)
# io.show()

cv2.imshow('image', (background - twotrucks))
cv2.waitKey()

cv2.imshow('image', (background - img))
cv2.waitKey()

cv2.imshow('image', (background - img2))
cv2.waitKey()
