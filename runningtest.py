from http.server import executable
from lib2to3.pgen2 import driver
import os
from tkinter import Button
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service

os.environ['PATH'] += r"C:\\Users\\cfmkm\\AppData\\Local\\Programs\\Python\\Python310\\geckodriver.exe"


def testinstagram():   
    driver = webdriver.Firefox()
    url = 'https://www.instagram.com/accounts/login/'
    driver.get(url)
    time.sleep(1.5)
    username = driver.find_element_by_name("username").send_keys("")
    password = driver.find_element_by_name("password").send_keys ("")
    logIn = driver.find_element_by_css_selector("button[type='submit'").click()
    time.sleep(2)
    saveLogin = driver.find_element_by_xpath(xpath = //* [@class='barone']) 
    
    
    input['Not Now']).click()
   
    
    return

testinstagram()

