# 这是一个获取谷歌搜索的前几条搜索结果的py

from ast import Not
from genericpath import exists
import webbrowser
import bs4, requests as rq, os, re, urllib
import logging

# from requests_html import HTMLSession

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)
headers = "headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}"


# # 构造一个Request对象，并禁用重定向和JavaScript
# req = rq.Request('GET', 'http://example.com',
#                         headers,
#                         allow_redirects=False)


search = input("你想搜什么")

url_g = "https://www.google.com/search?q=" + search


if os.path.exists("./3.html"):
    logging.info("文件存在")
else:
    web_g = rq.get(url_g, headers)
    try:
        web_g.raise_for_status
        with open("./3.html", "wb") as web_text:
            for i in web_g.iter_lines(10000):
                web_text.write(i)
                logging.info("写入完成")
    except Exception:
        logging.warning("出错了")

lists = []
with open("./3.html", "rb") as web_text:
    google_html = bs4.BeautifulSoup(web_text, "html.parser")
    hh = google_html.select("h3")

    for i in hh:
        print(i.getText())
    # 遍历所有的div元素，查找位于其上方的a元素
    for div in hh:
        str1 = div.parent.parent.parent.get("href")
        str1 = str(str1)
        url = re.compile(r"/url\?q=(.*?)(?=(&|$))")
        ss = url.match(str1)
        decoded_url = ""
        if ss is not None:
            decoded_url = urllib.parse.unquote(ss.group(1))
        ll = {}

        ll["title"] = div.getText()
        ll["url"] = decoded_url
        lists.append(ll)
for dict in lists:
    logging.info(dict)
i = 0
for dict in lists:
    if dict["url"] is not None:
        webbrowser.open(dict["url"])
        i += 1
    if i > 5:
        break
