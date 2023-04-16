import os, bs4

res = ""
with open("./web_scraping_information11\example.html", "r") as readWeb:
    # 这里注意要使用解析器，解析器有三种，html.parser，lxml，html5lib

    ll = bs4.BeautifulSoup(readWeb, "html.parser")
    type(ll)
    # 通过标签选择器进行选择，返回的是一个列表，于是用for循环
    for i in ll.select("p"):
        print(i.getText())
    for i in ll.select("#author"):
        print(i.attrs)
