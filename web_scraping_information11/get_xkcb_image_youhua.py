import logging
import os
import re
import time
from traceback import print_tb

import bs4
import requests


# 设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


def get_html(url):
    # 将HTML保存到本地文件
    with open("./4.html", "wb") as file_write:
        html = requests.get(url, headers=headers)
        for i in range(0, len(html.content), 1000):
            file_write.write(html.content[i : i + 1000])


def get_images():
    src_img = ""
    # 如果文件夹不存在，则创建
    if not os.path.exists("./img"):
        realpth = os.path.realpath("./img")
        logging.info("文件夹已存在:%s" % realpth)
        os.makedirs("./img")

    # 如果HTML文件不存在，则记录日志并退出函数
    if not os.path.exists("./4.html"):
        logging.warning("文件不存在")
        return

    # 从HTML文件中获取图片链接
    with open("./4.html", "rb") as file_read:
        soup = bs4.BeautifulSoup(file_read, "html.parser")
        div = soup.select("#comic")
        src_img = "https:" + div[0].img.get("src")
        logging.info(src_img)

    # 下载图片并保存到本地文件夹
    url_img = requests.get(src_img, headers=headers)
    file_name = os.path.basename(src_img)
    logging.info(f"图片地址:{src_img},文件名字:{file_name}")
    with open("./img/" + file_name, "wb") as write_img:
        for i in range(0, len(url_img.content), 1000):
            write_img.write(url_img.content[i : i + 1000])


def get_pre():
    # 从HTML文件中获取上一个链接
    with open("./4.html", "rb") as file_write:
        soup = bs4.BeautifulSoup(file_write, "html.parser")
        div = soup.select(".comicNav")
        a = div[0].find_all(rel="prev")
        url = "https://xkcd.com" + a[0].get("href")
        logging.info(f"下一个地址是:{url}")
        return url


if __name__ == "__main__":
    # 配置日志等级和格式
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    # 初始URL
    url = "https://xkcd.com/2059"

    # 循环下载并保存图片
    for i in range(4):
        try:
            get_html(url)
            get_images()
            url = get_pre()
            logging.info("暂停")
            time.sleep(10)
        except Exception as e:
            # 记录异常信息
            logging.exception(e)
