# Import required libraries
import numpy as np
from PIL import Image, ImageFilter, ImageOps
from scipy.spatial import KDTree

# Load the two images
img1 = Image.open('/content/Screenshot 2023-04-21 at 11.29.40 AM.png')
img2 = Image.open('/content/Screenshot 2023-04-21 at 11.29.50 AM.png')

# Convert the images to RGB format
rgb1 = img1.convert('RGB')
rgb2 = img2.convert('RGB')

# Get the dimensions of the images
width, height = img1.size


img1 = Image.open('/content/Screenshot 2023-04-21 at 11.29.40 AM.png')
img2 = Image.open('/content/Screenshot 2023-04-21 at 11.29.50 AM.png')

# Convert the images to RGB format
rgb1 = img1.convert('RGB')
rgb2 = img2.convert('RGB')

diff_pixels = np.absolute(np.asarray(rgb1).astype(np.uint16) - np.asarray(rgb2).astype(np.uint16))
diff_pixels = np.clip(diff_pixels,0, 256).astype(np.uint8)
diff_img = Image.fromarray(diff_pixels)


# # Create a KDTree of the pixel values in the difference image
# tree = KDTree(diff_pixels_arr[:, 1:], leafsize=10)

# # Find the closest pixel to each pixel in the difference image
# closest_pixels = []
# for x in range(width):
#     for y in range(height):
#         if diff_img.getpixel((x, y)) != (0, 0, 0):
#             query_point = np.array([x, y, *diff_img.getpixel((x, y))])
#             distance, index = tree.query(query_point[1:])
#             closest_pixels.append((x, y, tuple(diff_pixels_arr[index])))

# # Print the locations and closest RGB values of the differences
# for pixel in closest_pixels:
#     print(f"Location: ({pixel[0]}, {pixel[1]}), Closest RGB Value: {pixel[2][1:]}")

# Save the difference image as a file
diff_img.save('diff_image.jpg')
diff_img.show()

# Convert the image to grayscale
gray_image = ImageOps.grayscale(diff_img)

# Apply a median filter to remove noise
filtered_image = gray_image.filter(ImageFilter.MedianFilter(size=3))

# Apply an adaptive threshold to binarize the image
binary_image = filtered_image.point(lambda x: 255 if x > 65 else 0, mode='1')

# Remove small artifacts using erosion and dilation
kernel = ImageFilter.Kernel((3,3), [1,1,1,1,1,1,1,1,1])
eroded_image = binary_image.filter(ImageFilter.MinFilter(size=3))
dilated_image = eroded_image.filter(ImageFilter.MaxFilter(size=3))

# Save the grayscale image
dilated_image.save('gray_image.jpg')
dilated_image.show()

# Convert the image to grayscale
gray_image = ImageOps.grayscale(diff_img)

# Apply a median filter to remove noise
filtered_image = gray_image.filter(ImageFilter.MedianFilter(size=3))

# Apply an adaptive threshold to binarize the image
binary_image = filtered_image.point(lambda x: 255 if x > 65 else 0, mode='1')

# Remove small artifacts using erosion and dilation
kernel = ImageFilter.Kernel((3,3), [1,1,1,1,1,1,1,1,1])
eroded_image = binary_image.filter(ImageFilter.MinFilter(size=3))
dilated_image = eroded_image.filter(ImageFilter.MaxFilter(size=3))

# Save the grayscale image
dilated_image.save('gray_image.jpg')
dilated_image.show()