# -*- coding: utf-8 -*-
#download gechodriver https://github.com/mozilla/geckodriver/releases
#/usr/local/bin/geckodriver (in PATH)

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
firefox_capabilities['binary'] = '/Volumes/Untitled/Applications/Firefox.app/Contents/MacOS/firefox'
browser = webdriver.Firefox(capabilities=firefox_capabilities)
browser.get("https://www.google.com")
browser.quit()
