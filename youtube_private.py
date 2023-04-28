from seleniumwire.undetected_chromedriver.v2 import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time
from PIL import Image, ImageFilter, ImageOps

from image_difference_processing import get_people_pixels

from passwords import GMAIL_USERNAME, GMAIL_PASSWORD

# TO RUN THIS FILE
# Duplicate the file `passwords_template.py` and rename it to `passwords.py`.
# Type in your Gmail username and password where indicated. passwords.py should be in the .gitignore
# and therefore should not be committed to Github, but
# DOUBLE CHECK THAT YOU ARE NOT COMMITTING YOUR GMAIL PASSWORD BEFORE YOU PUSH!!!!

if __name__ == "__main__":

    options = {}
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--user-data-dir=hash')
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-dev-shm-usage")

    browser = Chrome(seleniumwire_options=options, options=chrome_options)
    wait = WebDriverWait(browser, 10)
    browser.get('https://gmail.com')
    wait.until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="identifierId"]'))).send_keys(GMAIL_USERNAME)
    wait.until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="identifierNext"]/div/button'))).click()
    time.sleep(5)
    wait.until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))).send_keys(GMAIL_PASSWORD)
    wait.until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="passwordNext"]/div/button'))).click()

    # It will ask you for your 2 factor authentication on your phone here.
    time.sleep(50)
    browser.get('https://www.youtube.com/watch?v=JIb4EGf5uFA')

    # Do initial truck processing
    initial_image_path = f'images/science_center{time.time()}.png'
    browser.save_screenshot(initial_image_path)
    truck_image = Image.open(initial_image_path)
    # TODO FINISHT HIS

    last_image_path = initial_image_path
    this_image_path = None
    while True:
        this_image_path = f'images/science_center{time.time()}.png'
        browser.save_screenshot(this_image_path)
        img1 = Image.open(this_image_path)
        img2 = Image.open(last_image_path)
        people_pixels = get_people_pixels(img1, img2)
        time.sleep(10)
        last_image_path = this_image_path

    browser.close()
