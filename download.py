# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from commen.configure import *
import unittest, time, re
import sys


def download(env):
	profile = webdriver.FirefoxProfile()
	profile.set_preference("browser.download.folderList", 2)
	profile.set_preference("browser.download.manager.showWhenStarting", False)
	profile.set_preference("browser.download.dir","C:\\");
	profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
	profile.set_preference("browser.download.panel.shown", True)
	browser = webdriver.Firefox(firefox_profile=profile)
	browser.implicitly_wait(30)
	browser.maximize_window()
	url = 'https://' + env + '.spotlightessentials.com/'
	browser.get(url)
	browser.find_element_by_link_text("Sign in").click()
	time.sleep(15)
	browser.find_element_by_id("username").click()
	browser.find_element_by_id("username").clear()
	username = get_keyvalue(env, "username")
	browser.find_element_by_id("username").send_keys(username)
	browser.find_element_by_id('password').click()
	browser.find_element_by_id("password").clear()
	password = get_keyvalue(env, "password")
	browser.find_element_by_id("password").send_keys(password)
	browser.find_element_by_id("kc-login").click()
	time.sleep(15)
	browser.find_element_by_xpath("//li[2]/a").click()
	browser.find_element_by_link_text("Account Settings").click()
	browser.find_element_by_link_text("Spotlight Tuning Pack").click()
	browser.find_element_by_link_text("Download").click()

if __name__ == "__main__":
	download(sys.argv[1])
