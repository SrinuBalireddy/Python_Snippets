# Write your code here :-)
#!python3
#CLEmail.py - reads email and message from CL and send an email using gmail

from selenium import webdriver
import sys

browser = webdriver.Chrome()
browser.get('https://www.gmail.com')
userElem = browser.find_element_by_css_selector('#identifierId')
userElem.send_keys('sowndarya.sri@gmail.com')
nextElem = browser.find_element_by_css_selector('#identifierNext > span > span')
nextElem.click()
