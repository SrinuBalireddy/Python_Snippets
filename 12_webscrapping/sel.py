# Write your code here :-)
"""
from selenium import webdriver

browser = webdriver.Chrome()
print(type(browser))
browser.get('https://inventwithpython.com')

elem = browser.find_element_by_css_selector('body > div.container > div:nth-child(6) > div > p:nth-child(2) > a')
print(elem.get_attribute('href'))
"""
"""
from selenium import webdriver
import os

browser = webdriver.Chrome()
browser.get('https://login.metafilter.com')
user = browser.find_element_by_id('user_name')
user.send_keys('username')

pwd = browser.find_element_by_id('user_pass')
pwd.send_keys('pwd')
pwd.submit()

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://nostarch.com')
htmlelem = browser.find_element_by_tag_name('html')
htmlelem.send_keys(Keys.END)
htmlelem.send_keys(Keys.HOME)
htmlelem.send_keys(Keys.PAGE_DOWN)
htmlelem.send_keys(Keys.RETURN)
elem = browser.find_element_by_css_selector('#node-487 > div.field.field-name-body.field-type-text-with-summary.field-label-hidden > div > div > p > a')
elem.click()
browser.back()
#browser.quit()



