from seleniumwire.undetected_chromedriver.v2 import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time

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

    while True:
        browser.save_screenshot(f'images/science_center{time.time()}.png')
        time.sleep(1)

    browser.close()
