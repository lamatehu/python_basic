import os
import re
import urllib.parse
import webbrowser
import logging
import requests
import bs4

# 配置日志
logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)

# 设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# 输入查询关键字
search_query = input("请输入查询关键字：")

# 构建 Google 搜索的 URL
google_search_url = f"https://www.google.com/search?q={search_query}"

# 检查是否存在已保存的 HTML 文件，如果存在，则直接使用该文件
if os.path.exists("./google_search_results.html"):
    logging.info("找到已保存的 HTML 文件")
else:
    # 否则，从 Google 搜索页面获取搜索结果并保存到文件中
    try:
        response = requests.get(google_search_url, headers=headers)
        response.raise_for_status()
        with open("./google_search_results.html", "wb") as html_file:
            for chunk in response.iter_content(10000):
                html_file.write(chunk)
                logging.info("已将搜索结果写入文件")
    except requests.exceptions.RequestException as e:
        logging.warning("获取搜索结果时出错：%s", e)

# 解析搜索结果 HTML 文件
search_results = []
with open("./google_search_results.html", "rb") as html_file:
    soup = bs4.BeautifulSoup(html_file, "html.parser")
    # 找到所有标题为 h3 的元素
    h3_elements = soup.select("h3")

    # 遍历 h3 元素并获取链接和标题
    for h3_element in h3_elements:
        parent_element = h3_element.parent.parent.parent
        href_str = parent_element.get("href")
        url_pattern = re.compile(r"/url\?q=(.*?)(?=(&|$))")
        url_match = url_pattern.match(str(href_str))
        decoded_url = ""
        if url_match is not None:
            decoded_url = urllib.parse.unquote(url_match.group(1))
        result = {"title": h3_element.getText(), "url": decoded_url}
        search_results.append(result)

# 打印所有搜索结果的标题和链接
for result in search_results:
    logging.info(result)

# 打开前五个搜索结果的链接
num_opened = 0
for result in search_results:
    if result["url"] is not None:
        webbrowser.open(result["url"])
        num_opened += 1
    if num_opened >= 5:
        break
