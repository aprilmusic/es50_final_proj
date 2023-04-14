import numpy as np
from PIL import Image
from scipy.spatial import KDTree

# Load the two images
img1 = Image.open('/content/science_center1680284125.821405.png')
img2 = Image.open('/content/science_center1680972203.6774762.png')

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
        diff = (abs(pix1[0] - pix2[0]), abs(pix1[1] - pix2[1]), abs(pix1[2] - pix2[2]))
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
diff_img.save('diff_image.jpg')
diff_img.show()