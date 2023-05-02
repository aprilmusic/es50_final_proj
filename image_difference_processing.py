import numpy as np
from PIL import Image, ImageFilter, ImageOps
from scipy.spatial import KDTree
from scipy import ndimage
from skimage.transform import resize
import matplotlib.pyplot as plt

import serial

import time

# Load the two images
img1 = Image.open('images/science_center1682444448.872606.png')
img2 = Image.open('images/science_center1682444452.3114848.png')
arduinoData = serial.Serial('/dev/cu.usbmodem101', 115200)


def get_people_pixels(img1, img2):
    ''' Returns pixels in form [x1, y1, x2, y2, ...] '''

    # Convert the images to RGB format
    rgb1 = img1.convert('RGB')
    rgb2 = img2.convert('RGB')

    # Get the dimensions of the images
    width, height = img1.size
    print(width, height)

    diff_pixels = np.absolute(np.asarray(rgb1).astype(
        np.uint16) - np.asarray(rgb2).astype(np.uint16))
    diff_pixels = np.clip(diff_pixels, 0, 256).astype(np.uint8)
    diff_img = Image.fromarray(diff_pixels)

    gray_image = ImageOps.grayscale(diff_img)

    # Apply a median filter to remove noise
    filtered_image = gray_image.filter(ImageFilter.MedianFilter(size=3))

    # Apply an adaptive threshold to binarize the image
    binary_image = filtered_image.point(
        lambda x: 255 if x > 65 else 0, mode='1')

    # Remove small artifacts using erosion and dilation
    kernel = ImageFilter.Kernel((3, 3), [1, 1, 1, 1, 1, 1, 1, 1, 1])
    eroded_image = binary_image.filter(ImageFilter.MinFilter(size=3))
    dilated_image = eroded_image.filter(ImageFilter.MaxFilter(size=3))

    dilated_image = np.asarray(dilated_image)

    # We'll add people to this array
    people_components = np.zeros(dilated_image.shape, dtype=np.float64)

    labeled, nr_objects = ndimage.label(dilated_image)
    for i in range(nr_objects):
        # If they're really small, skip them
        if np.sum(labeled == i+1) < 900:
            continue
        labeled_1 = np.zeros(labeled.shape) + (labeled == i+1)
        # plt.imshow(labeled_1)
        # plt.show()

        people_components += labeled_1

    pixels = resize(people_components, (32, 52))
    x, y = np.where(pixels > 0.1)
    coordinates = []
    print(x, y)
    for i in range(x.shape[0]):
        time.sleep(1)
        arduinoData.write(bytes(f'{y[i]:02d},{x[i]:02d}', 'utf-8'))

    # plt.imshow(pixels)
    # plt.show()

    return pixels


get_people_pixels(img1, img2)
