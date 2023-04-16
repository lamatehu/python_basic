# 文件组织练习
from fileinput import filename
import shutil
import os

import send2trash

file9 = os.path.abspath(".")
print(file9)
listdirs = os.listdir(os.path.abspath("."))
print(listdirs)
shutil.copy(file9 + "\\demo.py", file9 + "\\demo2.py")
print(listdirs)
shutil.move(file9 + "\\demo2.py", file9 + "\\demo3.py")
# os.mkdir(file9 + "\\hehe")
# os.removedirs(file9 + "\\hehe")
# shutil.rmtree(file9 + "\\hehe")

# 创建文件的小案例

try:
    for i in range(10):
        filename = file9 + "\\hehe\\{}.txt".format(i)
        with open(filename, "w"):
            print("文件{}创建成功".format(filename))
except FileExistsError:
    print("文件已创建")
dirs = os.listdir(file9 + "\\hehe")
for file in dirs:
    if file.endswith(".txt"):
        print(file)

# 删除文件到回收站

with open("a.txt", "w") as testb:
    print("创建成功")
    testb.write("ni hao")
send2trash.send2trash("a.txt")


for foldername, subfolder, filenames in os.walk(file9):
    print(foldername)
    print("----")
    print(subfolder)
    print("----")
    print(filenames)
