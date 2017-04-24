# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as beatsop
import re
# driver = webdriver.Chrome("chromedriver")
driver = webdriver.Firefox()
# driver.set_page_load_timeout(30)
driver.implicitly_wait(10)
driver.get('https://www.facebook.com/login.php?next=https%3A%2F%2Fwww.facebook.com%2Fsharer.php%3Fs%3D100%26p%255Burl%255D%3Dhttps%253A%252F%252Fdiplomtime.com%252Ffriend%252F405729&display=popup')



time.sleep(2)
try:
    n = driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    print(n)
    print "ok"
except NameError:
    print "no"



time.sleep(2)
try:
    element = driver.find_element_by_tag_name('body')
    # n = ActionChains(driver).move_to_element(element).key_down(Keys.CONTROL).send_keys('f').key_up(Keys.CONTROL).perform()
    n = ActionChains(driver).key_down(Keys.CONTROL).send_keys_to_element(element, 'f').key_up(Keys.CONTROL).perform()
    print(n)
    print 'ok'
except NameError:
    print 'no'


time.sleep(2)
try:
    n = driver.find_element_by_tag_name('body').send_keys(u'\ue031')
    print(n)
    print "ok"
except NameError:
    print 'no'



time.sleep(2)
try:
    n = driver.find_element_by_tag_name('body').send_keys(F5)
    print(n)
    print "ok"
except NameError:
    print(n)
    print 'no'



time.sleep(2)
try:
    n = driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'r')
    print(n)
    print "ok"
except NameError:
    print(n)
    print 'no'



time.sleep(2)
try:
    n = driver.find_element_by_xpath(".//*[@id='u_0_2']").click()
    print(n)
    print "ok"
except NameError:
    print(n)
    print 'no'






















# ActionChains(driver) \
#     .key_down(Keys.CONTROL) \
#     .click(element) \
#     .key_up(Keys.SHIFT) \
#     .perform() \