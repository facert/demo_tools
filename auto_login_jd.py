#! coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

name = '****'
password = '****'

driver = webdriver.Firefox()
driver.get("https://passport.jd.com/new/login.aspx")
elem_account = driver.find_element_by_name("loginname")
elem_password = driver.find_element_by_name("nloginpwd")
elem_account.clear()
elem_password.clear()
elem_account.send_keys(name)
elem_password.send_keys(password)

driver.find_element_by_id("loginsubmit").click()

