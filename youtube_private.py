import matplotlib.pyplot as plt
from seleniumwire.undetected_chromedriver.v2 import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time
from PIL import Image, ImageFilter, ImageOps

import numpy as np
import serial

from image_difference_processing import get_people_pixels, get_truck_prediction

from passwords import GMAIL_USERNAME, GMAIL_PASSWORD

# https://forum.arduino.cc/t/serial-input-basics/278284/2
# http://www.gammon.com.au/serial

if __name__ == "__main__":

    # options = {'ca_cert': 'ca.crt'}
    options = {}
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--user-data-dir=hash')
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--ignore-certificate-errors")

    browser = Chrome(seleniumwire_options=options, options=chrome_options)

    # TO RUN THIS PART
    # Duplicate the file `passwords_template.py` and rename it to `passwords.py`.
    # Type in your Gmail username and password where indicated. passwords.py should be in the .gitignore
    # and therefore should not be committed to Github, but
    # DOUBLE CHECK THAT YOU ARE NOT COMMITTING YOUR GMAIL PASSWORD BEFORE YOU PUSH!!!!

    # wait = WebDriverWait(browser, 10)
    # browser.get('https://gmail.com')
    # wait.until(ec.presence_of_element_located(
    #     (By.XPATH, '//*[@id="identifierId"]'))).send_keys(GMAIL_USERNAME)
    # wait.until(ec.presence_of_element_located(
    #     (By.XPATH, '//*[@id="identifierNext"]/div/button'))).click()
    # time.sleep(5)
    # wait.until(ec.presence_of_element_located(
    #     (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))).send_keys(GMAIL_PASSWORD)
    # wait.until(ec.presence_of_element_located(
    #     (By.XPATH, '//*[@id="passwordNext"]/div/button'))).click()
    # time.sleep(30)

    # It will ask you for your 2 factor authentication on your phone here.

    # Unlisted youtube video
    browser.get('https://www.youtube.com/watch?v=QBKk4TQi9KU')
    time.sleep(5)
    wait = WebDriverWait(browser, 10)
    wait.until(ec.presence_of_element_located(
        (By.CLASS_NAME, "html5-video-player")
    ))
    video_player = browser.find_element(By.CLASS_NAME, "html5-video-player")
    video_player.send_keys("f")

    # Private youtube video
    # browser.get('https://www.youtube.com/watch?v=JIb4EGf5uFA')

    time.sleep(12)
    # Do initial truck processing
    initial_image_path = f'images/science_center{time.time()}.png'
    browser.save_screenshot(initial_image_path)
    truck_image = Image.open(initial_image_path)

    truck_1_location = [[1000, 1600], [1500, 2600]]
    truck_2_location = [[800, 1200], [2200, 3000]]
    truck_3_location = [[600, 900], [2800, 3200]]

    img = np.asarray(truck_image.convert('RGB'))

    truck1 = Image.fromarray(img[truck_1_location[0][0]:truck_1_location[0][1],
                                 truck_1_location[1][0]:truck_1_location[1][1], :])
    truck2 = Image.fromarray(img[truck_2_location[0][0]:truck_2_location[0][1],
                                 truck_2_location[1][0]:truck_2_location[1][1], :])
    truck3 = Image.fromarray(img[truck_3_location[0][0]:truck_3_location[0][1],
                                 truck_3_location[1][0]:truck_3_location[1][1], :])

    truck1_color = get_truck_prediction(truck1, 1)
    time.sleep(1)
    truck2_color = get_truck_prediction(truck2, 2)
    time.sleep(1)
    truck3_color = get_truck_prediction(truck3, 3)
    print(truck1_color, truck2_color, truck3_color)

    last_image_path = initial_image_path
    this_image_path = None
    image_array = []

    while True:
        this_time = time.time()
        this_image_path = f'images/science_center_{time.time()}.png'
        browser.save_screenshot(this_image_path)
        img1 = Image.open(this_image_path)
        image_array.append(img1)
        print('this image size', img1.size)
        img2 = Image.open(last_image_path)
        print('this image size', img2.size)
        print(this_time)
        people_pixels = get_people_pixels(img1, img2)
        plt.imshow(people_pixels)
        plt.savefig(f'pixel_images/{this_time}_pixels.png')

        # time.sleep(5)
        last_image_path = this_image_path

    browser.close()
