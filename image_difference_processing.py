import numpy as np
from PIL import Image, ImageFilter, ImageOps
from scipy.spatial import KDTree
from scipy import ndimage
from skimage.transform import resize
import matplotlib.pyplot as plt

import serial

import time

# Load the two images
# img1 = Image.open('images/science_center1682444448.872606.png')
# img2 = Image.open('images/science_center1682444452.3114848.png')
# img3 = Image.open('images/science_center1683060386.765471.png')
# background = Image.open('images/background_5-3.png')
arduinoData = serial.Serial('/dev/cu.usbmodem1101', 115200)

x_boundary = 25
y1_boundary = 9
y2_boundary = 18
time_increment = 2


def get_wait_times(image):
    # Convert the images to RGB format
    rgb1 = image.convert('RGB')
    rgb2 = background.convert('RGB')

    width, height = image.size
    print(width, height)
    width, height = background.size
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
    eroded_image = binary_image.filter(ImageFilter.MinFilter(size=3))
    dilated_image = eroded_image.filter(ImageFilter.MaxFilter(size=3))

    dilated_image = np.asarray(dilated_image)

    people_pixels = resize(dilated_image, (32, 52))

    wait_times = [0, 0, 0]

    labeled, nr_objects = ndimage.label(people_pixels)
    for i in range(nr_objects):
        labeled_1 = np.zeros(labeled.shape) + (labeled == i+1)
        # plt.imshow(labeled_1)
        # plt.show()

        if labeled_1[x_boundary:, y2_boundary:].sum() > 0:
            wait_times[0] += time_increment
        elif labeled_1[x_boundary:, y1_boundary:y2_boundary].sum() > 0:
            wait_times[1] += time_increment
        elif labeled_1[x_boundary:, :y1_boundary].sum() > 0:
            wait_times[2] += time_increment

    print(wait_times)
    plt.imshow(labeled)
    plt.show()

    # arduinoData.write(bytes(f'w1{wait_times[0]}', 'utf-8'))
    # time.sleep(1)
    # arduinoData.write(bytes(f'w2{wait_times[1]}', 'utf-8'))
    # time.sleep(1)
    # arduinoData.write(bytes(f'w3{wait_times[2]}', 'utf-8'))

    return wait_times


def get_truck_prediction(truck_array, truck_number):
    median_color = np.median(truck_array, axis=(0, 1))
    print(f'truck{truck_number}')
    print(median_color)
    # print(median_color - np.array([138., 187., 211.]))

    if np.abs((median_color - np.array([138., 187., 211.])).sum()) < 100:
        arduinoData.write(bytes(f"t{truck_number}b", 'utf-8'))
        return f"truck{truck_number}blue"

    if np.abs((median_color - np.array([171., 155., 100.])).sum()) < 50:
        arduinoData.write(bytes(f"t{truck_number}y", 'utf-8'))
        return f"truck{truck_number}yellow"

    if np.abs((median_color - np.array([150., 110., 130.])).sum()) < 75:
        arduinoData.write(bytes(f"t{truck_number}r", 'utf-8'))
        return f"truck{truck_number}red"


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

    print(x, y)

    for i in range(x.shape[0]):
        time.sleep(1)

        arduinoData.write(bytes(f'{y[i]:02d},{x[i]:02d}', 'utf-8'))
        # print(f'{y[i]:02d},{x[i]:02d}')

    time.sleep(1)
    arduinoData.write(bytes('new', 'utf-8'))
    # plt.show()

    return pixels


if __name__ == "__main__":
    # get_people_pixels(img1, img2)
    img3.show()
    get_wait_times(img3)
