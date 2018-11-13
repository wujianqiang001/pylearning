# -*- coding:utf-8 -*-
__author__ = 'sumin'
import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# 引入ActionChains鼠标操作类
from selenium.webdriver.common.action_chains import ActionChains
#登录
driver.get("http://tstmobile.gwcslife.com/NGLife/")
time.sleep(5)
#driver.find_element_by_xpath("/html/body/div[5]/img").click()
time.sleep(5)
driver.maximize_window()
ActionChains(driver).key_down(Keys.CONTROL).send_keys('-').key_up(Keys.CONTROL).perform()
ActionChains(driver).key_down(Keys.CONTROL).send_keys('-').key_up(Keys.CONTROL).perform()
ActionChains(driver).key_down(Keys.CONTROL).send_keys('-').key_up(Keys.CONTROL).perform()
ActionChains(driver).key_down(Keys.CONTROL).send_keys('-').key_up(Keys.CONTROL).perform()
driver.find_element_by_id("userCode").send_keys("sh0000001")
driver.find_element_by_id("password").send_keys("Aa111111")
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="loginbtn"]').click()
#点击建议书
time.sleep(2)
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="subRisk"]/img').click()
#点击新增
time.sleep(10)
driver.implicitly_wait(15)
driver.find_element_by_xpath('//*[@id="addSuggest"]').click()
#设置投保被保人
time.sleep(5)
driver.implicitly_wait(15)
driver.find_element_by_id("insuName").send_keys("mimi")
#设置性别---------------------------------------------------------------写判断
driver.find_element_by_xpath('//*[@id="inscheckbox"]/div').click()
#出生日期
time.sleep(2)
# 直接上代码
# 日期值
js = "document.getElementById('insuBirthday').removeAttribute('disabled')"
driver.execute_script(js)
driver.find_element_by_id('insuBirthday').send_keys('1990-08-24')
time.sleep(2)
print(driver.find_element_by_id('insuBirthday').get_attribute('value'))
time.sleep(3)
#driver.find_element_by_xpath("/html/body/div[5]/div[1]/table/tbody/tr[4]/td[5]").click()

#driver.find_element_by_xpath('//*[@id="insuOccName"]').click()

time.sleep(2)
driver.find_element_by_id("insuOccName").click()
time.sleep(2)
#点击一般
time.sleep(5)
driver.find_element_by_xpath('//*[@id="A"]').click()
time.sleep(2)
#点击集团团体
driver.find_element_by_xpath('//*[@id="AA1"]/div/div[1]/span').click()
time.sleep(2)
#点击内勤人员
driver.find_element_by_xpath('//*[@id="A00"]/span').click()
time.sleep(2)
#点击确认
driver.find_element_by_id("subSelect").click()
#与被保人关系
# 先定位到下拉菜单
time.sleep(10)
driver.implicitly_wait(15)
drop_downn = driver.find_element_by_xpath('//*[@id="relaWithIns"]')
# 再对下拉菜单中的选项进行选择
time.sleep(10)
driver.implicitly_wait(15)
drop_downn.find_element_by_xpath('//*[@id="relaWithIns"]/option[2]').click()
time.sleep(2)
#点击下一步
driver.find_element_by_id("nextStep-pc").click()
#设计险种
#添加主险
time.sleep(10)
driver.implicitly_wait(15)
#点击添加主险====================================================================================================================？
#将页面滚动条拖到底部
# js="var q=document.documentElement.scrollTop=10000"
# driver.execute_script(js)
time.sleep(10)
driver.implicitly_wait(15)
#driver.find_element_by_xpath('//*[@id="global-content"]/div[1]/div/fieldset/div[1]/div[2]/div[3]')
time.sleep(20)


time.sleep(1)
driver.implicitly_wait(15)
driver.find_element_by_xpath('//*[@id="InsuranceType"]').click()
#主险
time.sleep(5)

ActionChains(driver).key_down(Keys.CONTROL).send_keys('-').key_up(Keys.CONTROL).perform()
driver.implicitly_wait(15)
driver.find_element_by_xpath('//*[@id="mainrisk2PC"]/div[1]/div').click()
#点击确认按钮
driver.find_element_by_id("affirmMainRisk").click()
#选择缴费方式
# 先定位到下拉菜单
time.sleep(10)
driver.implicitly_wait(15)
drop_downn = driver.find_element_by_xpath('//*[@id="PayIntv"]')
# 再对下拉菜单中的选项进行选择
time.sleep(10)
driver.implicitly_wait(15)
drop_downn.find_element_by_xpath('//*[@id="PayIntv"]/option[2]').click()
time.sleep(2)
driver.implicitly_wait(15)
#点击保额
driver.find_element_by_id("Amnt").send_keys("100000")
time.sleep(2)
driver.implicitly_wait(15)
#点击确定
driver.find_element_by_id("sureAddBtn").click()
#点击下一步
time.sleep(20)
driver.implicitly_wait(15)
driver.find_element_by_xpath('//*[@id="showProfit-pc"]').click()
#driver.find_element_by_id("showProfit-pc").click()
#点击确认
time.sleep(20)
driver.implicitly_wait(15)
driver.find_element_by_id("errorBtn").click()
#点击生成PDF
time.sleep(10)
driver.implicitly_wait(15)
driver.find_element_by_id("saveAndPrintButton").click()
#点击传统建议书
time.sleep(10)
driver.implicitly_wait(15)
driver.find_element_by_xpath('//*[@id="downLoadButtongea"]/img').click()
time.sleep(10)
print('ok')
driver.close()

