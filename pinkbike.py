from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from http.server import executable
from lib2to3.pgen2 import driver
import os
from tkinter import Button
import time


os.environ['PATH'] += r"C:\\Users\\cfmkm\\AppData\\Local\\Programs\\Python\\Python310\\geckodriver.exe"


def findingBikes():   
    driver = webdriver.Firefox()
    url = 'https://www.pinkbike.com/buysell'
    driver.get(url)
    buySell = driver.find_element_by_css_selector("div.group:nth-child(8) > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)").click()
    largeSize = driver.find_element_by_css_selector("#group_framesize_alias_4").click()
    wheelSize = driver.find_element_by_css_selector("#filterdata_wheelsize_8").click()
    shipWithinCountry = driver.find_element_by_css_selector("#filterdata_shipping_3").click()
    #search = driver.find_element_by_css_selector("input.pb-button:nth-child(1)").click()
    #url = 'https://www.chainreactioncycles.com/ca/en/road/jerseys-cycle/road-short-sleeve'
    #driver.get(url)
    
    
    return


"""
def findingJersey():
    driver = webdriver.Firefox()
    url = 'https://www.chainreactioncycles.com/ca/en/road/jerseys-cycle/road-short-sleeve'
    driver.get(url)
    accept = driver.find_element_by_css_selector(".clipped-list > li:nth-child(23) > a:nth-child(1) > span:nth-child(1)").click()
    sex = driver.find_element_by_css_selector("div.narrow_status:nth-child(6) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1) > span:nth-child(1)").click()
    seeMore = driver.find_element_by_css_selector("div.narrow_status:nth-child(7) > ul:nth-child(2) > li:nth-child(24) > div:nth-child(1) > span:nth-child(2)")
    sportful = driver.find_element_by_css_selector(".clipped-list > li:nth-child(23) > a:nth-child(1) > span:nth-child(1)").click()
    
    return()
"""



findingBikes()
#findingJersey()



    