# 获取xkcb的图片
import logging, requests as rq, os, bs4, re
from time import sleep
from traceback import print_tb
from opcode import opname

url = "https://xkcd.com/2059"
# 配置日志
logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)

# 设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


def get_html():
    with open("./4.html", "wb") as file_write:
        html = rq.get(url, headers)
        for i in range(0, len(html.content), 1000):
            file_write.write(html.content[i : i + 1000])


def get_images():
    src_img = ""
    if not os.path.exists("./img"):
        realpth = os.path.realpath("./img")
        logging.info("文件夹已存在:%s" % {realpth})
        os.makedirs("./img")

    if not os.path.exists("./4.html"):
        logging.warning("文件不存在")
    with open("./4.html", "rb") as file_read:
        soup = bs4.BeautifulSoup(file_read, "html.parser")
        div = soup.select("#comic")
        src_img = "https:" + div[0].img.get("src")
        logging.info(src_img)
    url_img = rq.get(src_img, headers)
    file_name = os.path.basename(src_img)
    logging.info("图片地址:%s,文件名字:%s" % (src_img, file_name))

    with open("./img/" + file_name, "wb") as write_img:
        for i in range(0, len(url_img.content), 1000):
            write_img.write(url_img.content[i : i + 1000])


def get_pre():
    with open("./4.html", "rb") as file_write:
        soup = bs4.BeautifulSoup(file_write, "html.parser")
        div = soup.select(".comicNav")
        a = div[0].find_all(rel="prev")
        global url
        url = "https://xkcd.com" + a[0].get("href")
        logging.info("下一个地址是:%s" % (url))
    logging.info("删除中")
    os.remove("./4.html")


for i in range(4):
    get_html()
    get_images()
    get_pre()
    logging.info("暂停")
    sleep(10)
