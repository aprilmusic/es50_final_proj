# Import required libraries
from PIL import Image
import numpy as np

# Load the image file
image = Image.open('image.jpg')

# Convert the image to grayscale for faster processing
gray = image.convert('L')

# Convert the grayscale image to a numpy array
img_array = np.array(gray, 'uint8')

# Initialize the Haar Cascade classifier for detecting faces
haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Detect faces in the image
faces = haar_cascade.detectMultiScale(img_array, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    draw_rect = ImageDraw.Draw(image)
    draw_rect.rectangle([(x, y), (x+w, y+h)], outline=(0, 255, 0))

# Display the image with the detected faces
image.show()
