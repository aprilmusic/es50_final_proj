import numpy as np
from PIL import Image, ImageFilter, ImageOps
from scipy.spatial import KDTree
from scipy import ndimage
import matplotlib.pyplot as plt

# Load the two images
img1 = Image.open('images/science_center1682444448.872606.png')
img2 = Image.open('images/science_center1682444452.3114848.png')


def get_diff_locations(img1, img2):

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

    # Save the grayscale image TODO DELETE THIS LATER
    dilated_image.save('gray_image.jpg')
    dilated_image.show()

    labeled, nr_objects = ndimage.label(np.asarray(dilated_image))
    for i in range(nr_objects):
        # If they're really small, skip them
        if np.sum(labeled == i+1) < 1100:
            continue
        labeled_1 = np.zeros(labeled.shape) + (labeled == i+1)
        plt.imshow(labeled_1)
        plt.show()
        # TODO CONVERT THESE TO PIXELS TO DISPLAY ON THE BOARD AND RETURN THOSE INSTEAD

    return np.asarray(dilated_image)


get_diff_locations(img1, img2)
