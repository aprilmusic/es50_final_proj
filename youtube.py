import os
from functools import partial
from multiprocessing.pool import Pool
from PIL import Image

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.youtube.com/watch?v=JIb4EGf5uFA")
# driver.sendKeys(" ")
# driver.sendKeys("f")
while True:
    driver.save_screenshot(f'images/science_center{time.time()}.png')
    time.sleep(1)
