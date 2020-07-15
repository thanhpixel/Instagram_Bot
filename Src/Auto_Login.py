from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime

import pandas as pd

def auto_login(webdriver, login_username, login_password):
    webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher') # Access Instagram login page
    sleep(3)
    
    # Navigate login infor box
    username = webdriver.find_element_by_name('username')
    username.send_keys('')
    username.send_keys(login_username)
    password = webdriver.find_element_by_name('password')
    password.send_keys('')
    password.send_keys(login_password)
    
    # Click log-in
    button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button > div')
    button_login.click()
    sleep(3)
    
    # Skip pop-up dialog 
    # Comment these lines out, if you don't get a pop up asking about notifications
    notnow = webdriver.find_element_by_css_selector('#react-root > section > main > div > div > div > section > div > button')
    notnow.click() 
    sleep(3)
    notnow2 = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
    notnow2.click()
    sleep(3)