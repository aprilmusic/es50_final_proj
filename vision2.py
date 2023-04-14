import numpy as np
from PIL import Image
from scipy.spatial import KDTree

import matplotlib.pyplot as plt
import imageio.v3 as iio
import skimage
from scipy import ndimage


# Load the two images
img1 = Image.open('images/science_center1680284125.821405.png')
img2 = Image.open('images/science_center1680972203.6774762.png')


def compute_difference(img1, img2):

    # Convert the images to RGB format
    rgb1 = img1.convert('RGB')
    rgb2 = img2.convert('RGB')

    # Get the dimensions of the images
    width, height = img1.size

    # Create a new image to store the difference
    diff_img = Image.new('RGB', (width, height), (0, 0, 0))

    # Loop over the pixels in the images
    diff_pixels = []
    for x in range(width):
        for y in range(height):
            # Get the pixel values at this location in each image
            pix1 = rgb1.getpixel((x, y))
            pix2 = rgb2.getpixel((x, y))
            # Compute the absolute difference between the pixel values
            diff = (abs(pix1[0] - pix2[0]),
                    abs(pix1[1] - pix2[1]), abs(pix1[2] - pix2[2]))
            # Set the corresponding pixel in the difference image
            diff_img.putpixel((x, y), diff)
            if diff != (0, 0, 0):
                diff_pixels.append((x, y, *diff))

    # Convert the list of pixels to a numpy array
    diff_pixels_arr = np.array(diff_pixels)

    # Create a KDTree of the pixel values in the difference image
    tree = KDTree(diff_pixels_arr[:, 1:], leafsize=10)

    # Find the closest pixel to each pixel in the difference image
    closest_pixels = []
    for x in range(width):
        for y in range(height):
            if diff_img.getpixel((x, y)) != (0, 0, 0):
                query_point = np.array([x, y, *diff_img.getpixel((x, y))])
                distance, index = tree.query(query_point[1:])
                closest_pixels.append((x, y, tuple(diff_pixels_arr[index])))

    # # Print the locations and closest RGB values of the differences
    # for pixel in closest_pixels:
    #     print(f"Location: ({pixel[0]}, {pixel[1]}), Closest RGB Value: {pixel[2][1:]}")

    # Save the difference image as a file
    diff_img.save('images/diff_image.jpg')
    diff_img.show()


def connected_components(filename, sigma=1.0, t=0.5, connectivity=2):
    # load the image
    image = iio.imread(filename)
    # convert the image to grayscale
    gray_image = skimage.color.rgb2gray(image)
    # denoise the image with a Gaussian filter
    blurred_image = skimage.filters.gaussian(gray_image, sigma=sigma)
    # mask the image according to threshold
    binary_mask = blurred_image < t
    # perform connected component analysis
    labeled_image, count = skimage.measure.label(binary_mask,
                                                 connectivity=connectivity, return_num=True)
    return labeled_image, count


img = Image.open('images/diff_image.jpg').convert('L')
img = np.asarray(img)
imgf = ndimage.gaussian_filter(img, 1)
threshold = 50

# find connected components
labeled, nr_objects = ndimage.label(imgf > threshold)
plt.imshow(labeled)

plt.show()
print(nr_objects)
print(labeled)

# Cycle through connected components
for i in range(nr_objects):
    # If they're really small, skip them
    if np.sum(labeled == i+1) < 1600:
        continue
    labeled_1 = np.zeros(labeled.shape) + (labeled == i+1)
    plt.imshow(labeled_1)
    plt.show()
