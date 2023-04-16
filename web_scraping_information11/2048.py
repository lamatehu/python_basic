# 有问题没有解决
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import logging
from selenium.webdriver.common.action_chains import ActionChains

gecko_path = "D:\webDriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=gecko_path)


def scan():
    list1 = []
    for i in range(4):
        list1.append([0, 0, 0, 0])
    patten = re.compile(r"(.*)?(\d)-(\d)")

    print("ss")
    la = browser.find_elements_by_css_selector(".tile-container")
    print(la)
    for i in la:
        print(i)
        lb = i.find_elements_by_css_selector(".tile")
        for i in lb:
            print(i.get_attribute("class"))
            j = i.find_element_by_css_selector(".tile-inner")
            j_text = j.get_attribute("textContent")
            logging.warning(j.text + "  " + j_text)

            g = patten.search(i.get_attribute("class"))
            if g is not None:
                print(g.group(3) + "hahaah " + g.group(2) + "j.text" + j.text)
                list1[int(g.group(3)) - 1][int(g.group(2)) - 1] = int(j_text)

        logging.info("ddfdfdfd")
        # list1[int(g.group(3))][int(g.group(2))] = 0
        for cow in list1:
            for j in cow:
                print(str(j) + " ", end="")
            print()


def play():
    browser.get("https://play2048.co/")
    ll = browser.find_element_by_tag_name("html")
    driver = browser
    while True:
        # 等待用户按下按键
        key = driver.wait.until(
            lambda driver: driver.find_element_by_tag_name("body")
        ).send_keys(Keys.NULL)

        # 模拟按键操作
        actions = ActionChains(driver)
        if key == "a":
            actions.send_keys(Keys.LEFT)
        elif key == "d":
            actions.send_keys(Keys.RIGHT)
        elif key == "w":
            actions.send_keys(Keys.UP)
        elif key == "s":
            actions.send_keys(Keys.DOWN)
        else:
            # 用户按下了其他键
            continue

        # 执行操作
        actions.perform()

        # 调用scan函数
        scan()


def scan():
    print("dd")

play()
