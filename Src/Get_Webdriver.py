from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime

import pandas as pd

def get_webdriver():
    global webdriver
    chromedriver_path = 'C:/bin/chromedriver.exe' # Change this to your own chromedriver path!
    webdriver = webdriver.Chrome(executable_path=chromedriver_path) # Use Chrome as default browser
    sleep(2)
    
    return webdriver