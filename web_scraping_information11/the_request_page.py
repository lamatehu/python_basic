import re
import requests

res = requests.get("http://www.gutenberg.org/cache/epub/1112/pg1112.txt")
type(res)
try:
    res.raise_for_status()
except Exception as ect:
    print("下载失败时及时终止程序")


res.status_code = requests.codes.ok
with open("./2.txt", "wb") as playfile:
    for i in res.iter_content(1000):
        playfile.write(i)

with open("./2.txt", "r") as readfile:
    while True:
        line = readfile.readline()
        if not line:
            break
        print(line)


print(len(res.text))
print(res.text[:20])
