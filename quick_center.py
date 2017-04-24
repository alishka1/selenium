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
driver.get("https://diplomtime.com/friend/405298")
driver.implicitly_wait(10)
# driver.maximize_window()

try:
	select = Select(driver.find_element_by_class_name('top_select_type'))
	select.select_by_visible_text('Реферат')
	print(u'1. Тип работы выбран реферат                    ОК')
except:
	print(u'1. Тип работы выбран реферат                    ОШИБКА')

try:
	driver.find_element_by_css_selector('.js--loadorder_top').click()
	print(u'2. Кнопка узнать                                ОК')
except:
	print(u'2. Кнопка узнать                                ОШИБКА')

try:
	send = driver.find_element_by_css_selector('.txt_theme')
	send.send_keys(u"Тест")
	print(u'3. Тест напечатан -                             ОК')
except:
	print(u'3. Тест напечатан -                             ОШИБКА')

try:
	driver.find_element_by_css_selector('.button.green.big-text.but_theme.but_theme_requir').click()
	print(u'4. Кнопка далее                                 ОК')
except:
	print(u'4. Кнопка далее                                 ОШИБКА')

time.sleep(2)

try:
	driver.find_element_by_css_selector('.tag.big-text.center.but_skip_requir').click()
	print(u'4. Кнопка пропустить                            ОК')
except:
	print(u'4. Кнопка пропустить                            ОШИБКА')

time.sleep(2)

try:
	driver.find_element_by_css_selector('.tag.big-text.center.but_skip_attach.but_skip_attach').click()
	print(u'5. Кнопка пропустить                            ОК')
except:
	print(u'5. Кнопка пропустить                            ОШИБКА')



time.sleep(2)

inp = driver.find_element_by_css_selector(".txt_promo")
value = inp.get_attribute('value')
print(value)
if value == u'405298':
	print u"6. Промо-код                                   ОК"
else:
	print u"6. Промо-код                                   ОШИБКА"

try:	
	send = driver.find_element_by_class_name('phone_rk')
	send.send_keys("77777777777")
	print(u'7. Телефон номер напечатан -                   ОК')
except:
	print(u'7. Телефон номер напечатан -                   ОШИБКА')


try:
	send = driver.find_element_by_class_name('email_rk')
	send.send_keys("test@diplomtime.ru")
	print(u'8. Email напечатан -                           ОК')
except:
	print(u'8. Email напечатан -                           ОШИБКА')

try:
	driver.find_element_by_css_selector('.button.green.big-text.but_call.but_next_call').click()
	print(u'9. Кнопка пропустить                            ОК')
except:
	print(u'9. Кнопка пропустить                            ОШИБКА')


time.sleep(2)


# element = driver.find_element_by_css_selector(".js__bonus_link")
# html = element.get_attribute("outerHTML")
# soup = BeautifulSoup(html, "html.parser")
# # anchors = soup.find_all('a', {'class': 'js__bonus_link', 'href': True})
# # for anchor in anchors:
# #     print (anchor['href'])
# anchors = soup.find('a', {'class': 'js__bonus_link', 'href': True})
# link = anchors['href']
# print(link)
# print(re.search('\w{5}://\w{10}.\w{3}/\w{6}/', link))

vk = '.sharediscount_modal__sharebutton.iconbase.iconsize40.iconvkcolor.js__soc_share'
element = driver.find_element_by_css_selector(vk)
ActionChains(driver) \
	.key_down(Keys.CONTROL) \
    .click(element) \
    .key_up(Keys.SHIFT) \
    .perform() \


time.sleep(5)
# try:
# 	driver.switch_to_window(driver.window_handles[1])
# 	print(u'ok')
# except:
# 	print(u'no')


try:
	driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+Keys.PAGE_UP)
	print(u'ok')
except:
	print(u'no')






# element = driver.find_element_by_css_selector('.js--loadorder_top')
# ActionChains(driver) \
#     .click(element) \
#     .perform()

# time.sleep(2)

# element = driver.find_element_by_css_selector('.but_skip_theme')
# ActionChains(driver) \
#     .click(element) \
#     .perform()






