from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests as rq
import time

gecko_path = "D:\webDriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=gecko_path)


def log_gmail():
    browser.get("https://gmail.com")
    ele = browser.find_element_by_css_selector("#identifierId")
    ele.send_keys("hello@gmail.com")
    c = browser.find_element_by_css_selector("#identifierNext > div > button")
    time.sleep(3)
    c.click()


def log_nostarch():
    browser.get("http://nostarch.com")
    ll = browser.find_element_by_tag_name("html")
    ll.send_keys(Keys.END)
    time.sleep(2)
    ll.send_keys(Keys.HOME)


def req():
    ll = rq.get("http://nostarch.com")
    print(ll.status_code)


req()
# log_nostarch()
