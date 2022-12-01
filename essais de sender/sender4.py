# coding=utf-8
from selenium import webdriver
 
driver = webdriver.Firefox()
driver.get("http://mail.google.com")
 
driver.find_element_by_id("identifierId").send_keys("bobpaslabobine")
