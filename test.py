import numpy as np
from PIL import Image, ImageFilter, ImageOps
from scipy.spatial import KDTree
from scipy import ndimage
from skimage.transform import resize
import matplotlib.pyplot as plt

import serial

import time

arduinoData = serial.Serial('/dev/cu.usbmodem1101', 115200)
# for i in range(3):
time.sleep(2)

# arduinoData.write(bytes(
# '10,10,12,12,14,14,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00', 'utf-8'))
# arduinoData.write(bytes("605040302010", 'utf-8'))
# arduinoData.write(bytes(';10,;12,;14,;16,;18,;20,', 'utf-8'))

# time.sleep(1)

# arduinoData.write(bytes('15,30', 'utf-8'))
# time.sleep(5)

# arduinoData.write(bytes('new', 'utf-8'))
# time.sleep(5)

# arduinoData.write(bytes('10,12', 'utf-8'))
# time.sleep(1)

# arduinoData.write(bytes('3,6', 'utf-8'))
# time.sleep(1)
# arduinoData.write(bytes('03,06', 'utf-8'))
time.sleep(1)

arduinoData.write(bytes('48,25', 'utf-8'))
time.sleep(1)

arduinoData.write(bytes('49,24', 'utf-8'))
time.sleep(1)

arduinoData.write(bytes('49,04', 'utf-8'))
time.sleep(1)

arduinoData.write(bytes('49,12', 'utf-8'))
time.sleep(1)

arduinoData.write(bytes('49,08', 'utf-8'))
time.sleep(1)
