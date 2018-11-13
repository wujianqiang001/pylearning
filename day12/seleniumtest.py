# coding=utf-8
import time
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
time.sleep(3)
Id = lambda d: driver.find_element_by_id("%s"%d)
# driver.find_element_by_id("su").click()
Id("kw").send_keys("bmh")
Id("su").click()
