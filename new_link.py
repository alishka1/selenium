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

driver = webdriver.Chrome("chromedriver")
driver.set_page_load_timeout(30)
driver.get("http://oauth.vk.com/authorize?client_id=-1&redirect_uri=http%3A%2F%2Fvk.com%2Fshare.php%3Furl%3Dhttps%3A%2F%2Fdiplomtime.com%2Ffriend%2F405729&display=widget")
driver.implicitly_wait(10)
driver.maximize_window()

vk = driver.current_url
result1 = re.search(r'\w{4}\:\/\/\w{5}.\w{2}.\w{3}', vk)
print result1.group(0)
if result1.group(0) == 'http://oauth.vk.com' :
	print u"ОК"
else:
	print u"ОШИБКА"


time.sleep(2)
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.get('https://connect.ok.ru/dk?st.cmd=OAuth2Login&st.layout=w&st.redirect=%252Fdk%253Fcmd%253DWidgetSharePreview%2526amp%253Bst.cmd%253DWidgetSharePreview%2526amp%253Bst.shareUrl%253Dhttps%25253A%25252F%25252Fdiplomtime.com%25252Ffriend%25252F405729&st.client_id=-1')
ok = driver.current_url
result1 = re.search(r'\w{5}\:\/\/\w{7}.\w{2}.\w{2}', ok)
print result1.group(0)
if result1.group(0) == 'https://connect.ok.ru' :
	print u"ОК"
else:
	print u"ОШИБКА"

# time.sleep(2)
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
# driver.get('https://telegram.me/share/url?url=https%3A%2F%2Fdiplomtime.com%2Ffriend%2F405729')
# driver.find_element_by_tag_name('body').send_keys(Keys.ALT + Keys.F4)
# telegram = driver.current_url
# result1 = re.search(r'\w{5}\:\/\/\w{8}.\w{2}', telegram)
# print result1.group(0)
# if result1.group(0) == 'https://telegram.me' :
# 	print u"ОК"
# else:
# 	print u"ОШИБКА"

time.sleep(2)
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.get('https://www.facebook.com/login.php?next=https%3A%2F%2Fwww.facebook.com%2Fsharer.php%3Fs%3D100%26p%255Burl%255D%3Dhttps%253A%252F%252Fdiplomtime.com%252Ffriend%252F405729&display=popup')
facebook = driver.current_url
result1 = re.search(r'\w{5}\:\/\/\w{3}.\w{8}.\w{3}', facebook)
print result1.group(0)
if result1.group(0) == 'https://www.facebook.com' :
	print u"ОК"
else:
	print u"ОШИБКА"

time.sleep(2)
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.get('https://twitter.com/intent/tweet?url=https%3A%2F%2Fdiplomtime.com%2Ffriend%2F405729&original_referer=')
twitter = driver.current_url
result1 = re.search(r'\w{5}\:\/\/\w{7}.\w{3}', twitter)
print result1.group(0)
if result1.group(0) == 'https://twitter.com' :
	print u"ОК"
else:
	print u"ОШИБКА"