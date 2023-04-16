from selenium import webdriver

gecko_path = "D:\webDriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=gecko_path)

browser.get("http://inventwithpython.com")
try:
    elem = browser.find_element_by_class_name("bookcover")
    print("Found <%s> element with that class name!" % (elem.tag_name))
except:
    print("Was not able to find an element with that name.")

link = browser.find_element_by_css_selector('a.btn.btn-primary[href="#scratch"]')

link.click()
